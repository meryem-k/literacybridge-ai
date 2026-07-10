import re
import streamlit as st

st.set_page_config(page_title="Writing Practice", page_icon="🖊️")


def analyze_writing(text):
    """Detect writing skills and grammar/punctuation issues in a student response."""
    text_lower = text.lower().strip()
    word_count = len(text.split())
    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    sentence_count = len(sentences)

    # Evidence — quotation marks OR standard citation phrases
    evidence_phrases = [
        "the text states", "the passage states", "according to",
        "for example", "in the passage", "the author writes",
        "the text says", "in paragraph", "the author includes",
        "the author states", "as stated in",
    ]
    has_evidence = '"' in text or any(p in text_lower for p in evidence_phrases)

    # Explanation — explanation connectors
    explanation_phrases = [
        "this shows", "this means", "this suggests", "this reveals",
        "this tells", "this demonstrates", "this proves", "this indicates",
        "because of this", "in other words", "as a result",
        "this is important because", "this matters because",
    ]
    explanation_words = ["because", "therefore", "thus", "consequently"]
    has_explanation = (
        any(p in text_lower for p in explanation_phrases)
        or any(w in text_lower for w in explanation_words)
    )

    # Connection back to the prompt
    connection_phrases = [
        "therefore", "this proves", "ultimately", "in conclusion",
        "this demonstrates", "overall", "in summary", "in the end",
        "this confirms", "this shows that the author",
    ]
    has_connection = any(p in text_lower for p in connection_phrases)

    # Length
    is_adequate  = word_count >= 40
    is_developed = word_count >= 60

    # Sentence structure signals
    has_multiple_sentences = sentence_count >= 3
    starts_capital = text[0].isupper() if text else False
    ends_with_punct = text[-1] in ".!?" if text else False

    # Prompt answered — keyword check (separate from length so short answers still get credit)
    prompt_keywords = ["elena", "audition", "family", "fear", "courage",
                       "author", "shows", "text", "perform", "memory", "memories"]
    keyword_hits = sum(1 for w in prompt_keywords if w in text_lower)
    answers_prompt = keyword_hits >= 2

    # ── Grammar and punctuation detection ──────────────────────────────────────

    grammar_issues = []

    # 1. Unnecessary comma after subordinating "that"
    #    e.g. "shows that, Elena's..." — comma does not belong here
    if re.search(r"\bthat,\s", text):
        grammar_issues.append({
            "label": "Unnecessary Comma After \"that\"",
            "teach": (
                "There is a comma after the word \"that\" where one does not belong. "
                "A comma should not separate \"that\" from the clause it introduces."
            ),
            "correct": (
                "Remove the comma. Write: \"shows that Elena's\" — not \"shows that, Elena's.\""
            ),
        })

    # 2. Character name misspelled — "Elen's" instead of "Elena's"
    if re.search(r"\bElen's\b", text) and not re.search(r"\bElena's\b", text):
        grammar_issues.append({
            "label": "Character Name Spelling",
            "teach": (
                "The character's name is spelled \"Elena,\" not \"Elen.\" "
                "Spelling a character's name incorrectly in an SCR is an editing error."
            ),
            "correct": "Change \"Elen's\" to \"Elena's\".",
        })

    # 3. Missing apostrophe in possessive — "Elenas" with no apostrophe
    if re.search(r"\bElenas\b", text):
        grammar_issues.append({
            "label": "Missing Apostrophe in Possessive",
            "teach": (
                "\"Elena's\" needs an apostrophe because it shows possession — "
                "something belongs to Elena. Without the apostrophe, \"Elenas\" looks "
                "like a plural noun, not a possessive."
            ),
            "correct": "Change \"Elenas\" to \"Elena's\".",
        })

    # 4. Wordiness — "noun + that + pronoun" where "that" can be dropped
    #    e.g. "memories that she recalls" → "memories she recalls"
    if re.search(
        r"\b(memories|details|moments|events|scenes|ideas)\s+that\s+(she|he|they|Elena)\b",
        text_lower,
    ):
        grammar_issues.append({
            "label": "Wordiness — Remove Extra \"that\"",
            "teach": (
                "The word \"that\" before \"she recalls\" (or similar) is not needed. "
                "Removing it makes your sentence shorter and cleaner without changing the meaning."
            ),
            "correct": (
                "Change \"memories that she recalls\" to \"memories she recalls.\""
            ),
        })

    return {
        "word_count":             word_count,
        "sentence_count":         sentence_count,
        "sentences":              sentences,
        "has_evidence":           has_evidence,
        "has_explanation":        has_explanation,
        "has_connection":         has_connection,
        "is_adequate":            is_adequate,
        "is_developed":           is_developed,
        "has_multiple_sentences": has_multiple_sentences,
        "starts_capital":         starts_capital,
        "ends_with_punct":        ends_with_punct,
        "answers_prompt":         answers_prompt,
        "grammar_issues":         grammar_issues,
    }


def suggest_revision(text, grammar_issues):
    """
    Apply detected grammar corrections to the student's first sentence
    to produce a 'Try revising like this' example.
    Returns the corrected first sentence, or empty string if no changes needed.
    """
    if not text:
        return ""

    sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    first = sentences[0] if sentences else text

    revised = first

    # Apply each detected fix in order
    for issue in grammar_issues:
        label = issue["label"]
        if "Unnecessary Comma" in label:
            revised = re.sub(r"\bthat,\s", "that ", revised)
        if "Character Name Spelling" in label:
            revised = re.sub(r"\bElen's\b", "Elena's", revised)
        if "Missing Apostrophe" in label:
            revised = re.sub(r"\bElenas\b", "Elena's", revised)
        if "Wordiness" in label:
            revised = re.sub(
                r"\b(memories|details|moments|events|scenes|ideas)\s+that\s+(she|he|they|Elena)\b",
                lambda m: f"{m.group(1)} {m.group(2)}",
                revised,
                flags=re.IGNORECASE,
            )

    if revised and revised[-1] not in ".!?":
        revised += "."

    # Only return if the revision is actually different from the original
    original_norm = first.rstrip(".!?") + "."
    if revised == original_norm:
        return ""
    return revised


# ─── Page Header ─────────────────────────────────────────────────────────────
st.title("🖊️ Short-Constructed Response Writing")
st.markdown(
    "Practice writing a short-constructed response (SCR). "
    "Work through the support tools below **before** you start writing."
)

# ─── Writing Prompt ──────────────────────────────────────────────────────────
st.subheader("📋 Writing Prompt")
st.caption("Connected to: *The Audition* — Literary Fiction (Passage 2)")
st.info(
    "**How does the author show that Elena's connection to her family gives her "
    "the courage to perform? Use evidence from the text to support your answer.**\n\n"
    "Write your response in **4–6 complete sentences**. "
    "Include a direct quote or specific detail from the passage."
)

# ─── Writing Support Tools ───────────────────────────────────────────────────
st.subheader("🛠️ Writing Support — Use These Before You Start")

tab_ace, tab_race = st.tabs(["ACE Framework", "RACE Framework"])

with tab_ace:
    st.markdown("""
**ACE** is a 3-step plan for writing a short-constructed response.

| Letter | Stands For | What To Do |
|--------|-----------|------------|
| **A** | **Answer** | Answer the question directly in your very first sentence. Don't make the reader wait. |
| **C** | **Cite** | Add proof from the text — a direct quote or a specific detail. Put quotes in quotation marks. |
| **E** | **Explain** | Explain HOW your evidence answers the question. This is the most important part. Don't just drop a quote — connect it to your answer. |

> 💡 **The most common mistake:** Students include a quote (C) but forget to explain it (E).
> The grader wants to know *what you think* the evidence means — not just what it says.
""")

with tab_race:
    st.markdown("""
**RACE** is a 4-step plan that adds a Restatement at the beginning.

| Letter | Stands For | What To Do |
|--------|-----------|------------|
| **R** | **Restate** | Rewrite the question in your own words as your first sentence. |
| **A** | **Answer** | Answer the question clearly and directly. |
| **C** | **Cite** | Add a direct quote or specific detail from the text. |
| **E** | **Explain** | Explain how your evidence connects to your answer. |

> 💡 **When to use RACE vs ACE:** Use RACE if your teacher specifically asks for a restatement.
> Both frameworks work — the key is always the same: **Answer → Evidence → Explanation**.
""")

with st.expander("💬 Sentence Stems — Copy and complete these to help you start"):
    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("**A — Answer the question**")
        st.code(
            "The author shows that...\n"
            'In "The Audition," Elena demonstrates...\n'
            "The text suggests that...\n"
            "According to the passage,...",
            language=None,
        )
        st.markdown("**C — Cite your evidence**")
        st.code(
            'For example, the text states, "..."\n'
            'In the story, the author writes, "..."\n'
            "The author includes the detail that...\n"
            'This is supported by the line "..."',
            language=None,
        )

    with col_right:
        st.markdown("**E — Explain your evidence**")
        st.code(
            "This shows that...\n"
            "This means that...\n"
            "This suggests that...\n"
            "This reveals that...\n"
            "Because of this,...\n"
            "In other words,...",
            language=None,
        )
        st.markdown("**Connect back to the prompt**")
        st.code(
            "Therefore, the author demonstrates...\n"
            "This proves that...\n"
            "Ultimately,...\n"
            "This confirms that...",
            language=None,
        )

with st.expander("📄 See a Sample Strong Response — With Labels"):
    st.markdown("""
> **Prompt:** How does the author show that Elena's connection to her family gives her the courage to perform?

---

🟦 **[A — Answer the question]**
> *The author shows that Elena's connection to her family gives her the courage to perform through the memories that surface at her moment of greatest fear.*

🟩 **[C — Cite evidence]**
> *For example, when Elena first opens her mouth and "nothing came," she immediately thinks of "her grandmother's church, candles, and her mother's hands in her hair."*

🟨 **[E — Explain the evidence]**
> *This shows that Elena does not find courage through practice or willpower, but through the emotional warmth of her family's memory.*

🟥 **[E — Connect back to the prompt]**
> *Her family connection acts as an anchor that pulls her back from fear and allows her voice to emerge, demonstrating that a sense of belonging can be more powerful than any amount of preparation.*

---
**Why this response earns full credit:**
- **A:** Answers the question in the very first sentence — no waiting
- **C:** Uses a specific, accurate quote with quotation marks
- **E:** Explains what the quote *means* — does not just repeat it
- **Connection:** Ends with a sentence that ties the evidence back to the bigger idea
""")

# ─── Student Writing Area ────────────────────────────────────────────────────
st.divider()
st.subheader("✏️ Your Response")
st.markdown("Write your own response below. Use the stems and sample above as a guide.")

if "writing_submitted" not in st.session_state:
    st.session_state.writing_submitted = False

response = st.text_area(
    "Type your short-constructed response here:",
    height=220,
    placeholder="Start with: The author shows that...",
    key="scr_response",
    disabled=st.session_state.writing_submitted,
)

word_count = len(response.split()) if response.strip() else 0

if word_count == 0:
    st.caption("Word count: 0  |  Aim for at least 40 words (4–6 sentences)")
elif word_count < 40:
    st.caption(f"Word count: {word_count}  |  ⚠️ Keep writing — aim for at least 40 words")
elif word_count < 60:
    st.caption(f"Word count: {word_count}  |  ✅ Good start — consider adding more explanation")
else:
    st.caption(f"Word count: {word_count}  |  ✅ Well-developed length")

# ─── Self-Assessment Checklist ───────────────────────────────────────────────
st.subheader("✅ Self-Assessment Checklist")
st.markdown("Check each box **before you submit** to make sure your response is complete:")

check1 = st.checkbox("I answered the question directly.")
check2 = st.checkbox("I cited text evidence (a direct quote or specific detail).")
check3 = st.checkbox("I explained how the evidence supports my answer.")
check4 = st.checkbox("I used complete sentences.")
check5 = st.checkbox("I connected my evidence back to the prompt.")

checks_done = sum([check1, check2, check3, check4, check5])
if checks_done > 0:
    st.caption(f"{checks_done}/5 checklist items complete")

# ─── Submit Button ────────────────────────────────────────────────────────────
if not st.session_state.writing_submitted:
    if response.strip():
        if st.button("Submit My Response", type="primary"):
            st.session_state.writing_submitted = True
            st.session_state.final_response = response
            st.rerun()
    else:
        st.caption("Type your response above to enable the Submit button.")

# ─── Feedback Section ─────────────────────────────────────────────────────────
if st.session_state.writing_submitted:
    final_text = st.session_state.get("final_response", "")
    analysis   = analyze_writing(final_text)

    st.divider()
    st.subheader("📊 Writing Skill Feedback")

    # ── Skill tags (quick overview) ───────────────────────────────────────────
    skills = {
        "Answering the Prompt":  analysis["answers_prompt"],
        "Citing Evidence":       analysis["has_evidence"],
        "Explaining Evidence":   analysis["has_explanation"],
        "Connecting Back":       analysis["has_connection"],
        "Adequate Length":       analysis["is_adequate"],
        "Sentence Clarity":      analysis["has_multiple_sentences"] and analysis["starts_capital"],
    }
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    for i, (skill, present) in enumerate(skills.items()):
        if present:
            cols[i % 3].success(f"✅ {skill}")
        else:
            cols[i % 3].warning(f"⚠️ {skill}")

    # ── Strengths ─────────────────────────────────────────────────────────────
    st.divider()
    strengths = []

    if analysis["answers_prompt"]:
        strengths.append(
            "You answered the prompt — your response shows that you understood the question "
            "and focused on Elena's family connection and courage."
        )
    if analysis["has_evidence"]:
        strengths.append("You included text evidence from the passage to support your answer.")
    if analysis["has_explanation"]:
        strengths.append("You explained how your evidence connects to the answer.")
    if analysis["has_connection"]:
        strengths.append("You connected your response back to the prompt at the end.")
    if analysis["is_developed"]:
        strengths.append("Your response is well-developed in length.")

    if strengths:
        st.success("**What you did well:**\n\n" + "\n".join(f"- {s}" for s in strengths))
    elif not analysis["answers_prompt"]:
        st.info(
            "**Getting started:** Make sure your first sentence directly answers the question. "
            "Try starting with: *The author shows that Elena's connection to her family...*"
        )

    # ── Build priority feedback queue (ACE order, max 2 structure + 1 grammar = 3 total) ──
    structure_recs = []

    # A — Did they answer? (only flag if truly missing)
    if not analysis["answers_prompt"] and not analysis["has_evidence"] and not analysis["has_explanation"]:
        structure_recs.append({
            "label": "📝 A — Answer the Prompt First",
            "body": (
                "Your first sentence should directly answer the question. "
                "Don't make the reader guess what you think.\n\n"
                "**Try this starter:** *The author shows that Elena's connection to her family "
                "gives her the courage to perform through...*"
            ),
            "next_step": "Write a first sentence that directly answers the question.",
        })

    # C — Evidence (most critical missing piece when answer is present)
    if not analysis["has_evidence"]:
        structure_recs.append({
            "label": "📌 C — Add Text Evidence",
            "body": (
                "Your response answers the question, but it needs a quote or specific detail "
                "from *The Audition* to prove your point. Without evidence, the reader has to "
                "take your word for it.\n\n"
                "**Try this:** Find a line from the passage that shows Elena thinking of her family "
                "during the audition. Copy it exactly and put it in quotation marks.\n\n"
                "*Starter: For example, the text states, \"...\"*"
            ),
            "next_step": (
                "Add a direct quote or specific detail from *The Audition* — "
                "something that shows Elena drawing on her family memory."
            ),
        })

    # E — Explanation (only flag if evidence is present but explanation missing)
    if analysis["has_evidence"] and not analysis["has_explanation"]:
        structure_recs.append({
            "label": "🔍 E — Explain Your Evidence",
            "body": (
                "You included evidence — that's great. Now explain what it *means*. "
                "Never just drop a quote and move on. Tell the reader why that quote matters.\n\n"
                "**Try this:** Right after your quote, add a sentence that starts with:\n"
                "- *This shows that...*\n"
                "- *This means that...*\n"
                "- *This reveals that...*"
            ),
            "next_step": (
                "After your quote, add a sentence explaining what the evidence shows "
                "about Elena's relationship with her family."
            ),
        })

    # Connect back (lower priority — only if other structure pieces are in place)
    if analysis["has_evidence"] and not analysis["has_connection"]:
        structure_recs.append({
            "label": "🔗 Connect Back to the Prompt",
            "body": (
                "Try ending your response with a sentence that ties your evidence back "
                "to the original question. This shows the reader you understand the big picture.\n\n"
                "**Try this:**\n"
                "- *Therefore, the author shows that...*\n"
                "- *This proves that...*\n"
                "- *Ultimately,...*"
            ),
            "next_step": (
                "Add a closing sentence that connects your evidence back to the idea "
                "of family giving Elena courage."
            ),
        })

    # Elaboration — only flag if the answer is present but response is very short
    if analysis["answers_prompt"] and not analysis["is_adequate"] and not structure_recs:
        structure_recs.append({
            "label": "📏 Develop Your Response Further",
            "body": (
                f"Your response is {analysis['word_count']} words. "
                "A strong SCR is usually 40–80 words — about 4–6 sentences.\n\n"
                "**Try this:** Go back and add more detail after your evidence. "
                "Ask yourself: *Why does this moment matter? What does it tell us about Elena?*"
            ),
            "next_step": "Expand your explanation — add a sentence about what the evidence reveals.",
        })

    # Grammar issues — take max 1 to show alongside structure feedback
    grammar_shown = analysis["grammar_issues"][:1]

    # Combine and cap at 3 total recommendations
    all_recs = structure_recs[:2] + [
        {
            "label": f"✏️ Grammar/Punctuation — {g['label']}",
            "body": f"**Notice this:** {g['teach']}\n\n**Correction:** {g['correct']}",
            "next_step": None,
            "is_grammar": True,
        }
        for g in grammar_shown
    ]
    shown_recs = all_recs[:3]

    # ── Display recommendations ───────────────────────────────────────────────
    if shown_recs:
        st.divider()
        st.subheader("🎯 Feedback")

        for rec in shown_recs:
            st.warning(f"**{rec['label']}**\n\n{rec['body']}")

        # Next Best Step — from first structure recommendation
        first_structure = next((r for r in shown_recs if not r.get("is_grammar")), None)
        if first_structure and first_structure.get("next_step"):
            st.info(f"**🚀 Your Next Best Step:** {first_structure['next_step']}")

        # Try Revising Like This — only if grammar issues were detected
        suggested = suggest_revision(final_text, analysis["grammar_issues"])
        if suggested:
            st.divider()
            st.markdown("**✏️ Try Revising Like This:**")
            st.markdown(
                f"> {suggested}\n\n"
                "*This example shows how to fix the punctuation and wording in your first sentence. "
                "Use it as a guide — write the revision in your own words.*"
            )

    else:
        st.divider()
        st.success(
            "Your response demonstrates strong writing skills across all areas. "
            "Review your skill tags above to see what you did well."
        )

    # ── Submitted response ────────────────────────────────────────────────────
    st.divider()
    st.markdown("**Your submitted response:**")
    st.markdown(f"> {final_text}")
    st.caption(
        f"Word count: {analysis['word_count']}  |  "
        f"Sentences detected: {analysis['sentence_count']}"
    )

    col_revise, col_new = st.columns(2)
    with col_revise:
        if st.button("✏️ Revise My Response"):
            st.session_state.writing_submitted = False
            if "final_response" in st.session_state:
                del st.session_state["final_response"]
            st.rerun()
    with col_new:
        if st.button("🔄 Start Over"):
            st.session_state.writing_submitted = False
            for key in ["final_response", "scr_response"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()
