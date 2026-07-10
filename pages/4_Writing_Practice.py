import re
import streamlit as st

st.set_page_config(page_title="Writing Practice", page_icon="🖊️")


def analyze_writing(text):
    """Detect which writing skills appear present in the student's response."""
    text_lower = text.lower().strip()
    word_count = len(text.split())

    # Sentence count (rough split on ending punctuation)
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
    starts_capital  = text[0].isupper() if text else False
    ends_with_punct = text[-1] in ".!?" if text else False

    # Rough "answered the prompt" check — prompt keywords present
    prompt_keywords = ["elena", "audition", "family", "fear", "courage",
                       "author", "shows", "text", "perform", "memory", "memories"]
    keyword_hits = sum(1 for w in prompt_keywords if w in text_lower)
    answers_prompt = keyword_hits >= 2 and is_adequate

    return {
        "word_count":             word_count,
        "sentence_count":         sentence_count,
        "has_evidence":           has_evidence,
        "has_explanation":        has_explanation,
        "has_connection":         has_connection,
        "is_adequate":            is_adequate,
        "is_developed":           is_developed,
        "has_multiple_sentences": has_multiple_sentences,
        "starts_capital":         starts_capital,
        "ends_with_punct":        ends_with_punct,
        "answers_prompt":         answers_prompt,
    }


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

# ACE / RACE framework explanation
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

# Sentence Stems
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

# Sample Strong Response
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
    st.markdown("Here is what your response shows about your writing skills:")

    # --- Skill Tags ---
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

    # --- Personalized Recommendations ---
    st.divider()
    st.subheader("🎯 Personalized Recommendations")

    recommendations_given = 0

    if not analysis["is_adequate"]:
        st.error(
            f"**📏 Elaboration Practice Needed**\n\n"
            f"Your response is {analysis['word_count']} word(s). "
            "A strong SCR is usually 40–80 words — about 4–6 sentences.\n\n"
            "**Try this:** Go back and add more detail to your explanation. "
            "Ask yourself: *Why does this evidence matter? What does it tell us about "
            "the character or the author's message?*"
        )
        recommendations_given += 1

    if not analysis["has_evidence"]:
        st.warning(
            "**📌 Citing Evidence Practice Needed**\n\n"
            "Your response does not appear to include a direct quote or text reference.\n\n"
            "**Try this:** Find one sentence or phrase in *The Audition* that supports "
            "your answer. Copy it exactly and put it in quotation marks. "
            'Use this starter: *For example, the text states, "..."*'
        )
        recommendations_given += 1

    if not analysis["has_explanation"]:
        st.warning(
            "**🔍 Explaining Evidence Practice Needed**\n\n"
            "Your response may include evidence but is missing an explanation of what it means.\n\n"
            "**Try this:** After your quote, add a sentence that starts with one of these:\n"
            "- *This shows that...*\n"
            "- *This means that...*\n"
            "- *This is important because...*\n\n"
            "Never just drop a quote — always explain what it proves."
        )
        recommendations_given += 1

    if not analysis["has_connection"]:
        st.info(
            "**🔗 Connecting Back to the Prompt**\n\n"
            "Try ending your response with a sentence that ties your evidence back "
            "to the original question.\n\n"
            "**Try this:** Close your response with one of these:\n"
            "- *Therefore, the author shows that...*\n"
            "- *This proves that...*\n"
            "- *Ultimately,...*"
        )
        recommendations_given += 1

    if not analysis["has_multiple_sentences"]:
        st.warning(
            "**📝 Sentence Structure Practice Needed**\n\n"
            "Your response appears to have fewer than 3 complete sentences. "
            "A full SCR needs at least 4 sentences — one for each part of ACE.\n\n"
            "**Try this:** Make sure each sentence ends with a period. "
            "Write a separate sentence for your Answer, your Evidence, "
            "your Explanation, and your Connection."
        )
        recommendations_given += 1

    if recommendations_given == 0:
        st.success(
            "Your response demonstrates strong writing skills across all areas. "
            "Review your skill tags above to see what you did well."
        )

    # --- Their submitted response ---
    st.divider()
    st.markdown("**Your submitted response:**")
    st.markdown(f"> {final_text}")
    st.caption(f"Word count: {analysis['word_count']}  |  Sentences detected: {analysis['sentence_count']}")

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
