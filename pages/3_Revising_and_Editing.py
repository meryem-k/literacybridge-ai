import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.revising_editing import EXERCISES

st.set_page_config(page_title="Revising & Editing", page_icon="✏️")

# ── Skill-based personalized recommendations ──────────────────────────────────
SKILL_RECOMMENDATIONS = {
    "Strengthening a Claim": (
        "**Practice writing stronger claims.** A strong claim states your position AND gives a reason. "
        "Try this: take a weak statement like 'Social media is popular' and rewrite it as an argument: "
        "'Social media should be limited for students because it reduces focus and increases anxiety.'"
    ),
    "Transitions": (
        "**Practice choosing transitions.** Learn the four types: "
        "*contrast* (however, although, yet), "
        "*cause-effect* (therefore, as a result, consequently), "
        "*addition* (furthermore, in addition, also), "
        "*illustration* (for example, for instance, specifically). "
        "Before choosing a transition, decide which relationship fits the sentences."
    ),
    "Adding Supporting Details": (
        "**Practice adding supporting details.** After each main idea, ask: "
        "'How do I know this is true? Can I give an example or a statistic?' "
        "A strong supporting detail directly proves the sentence above it — it does not introduce a new topic."
    ),
    "Removing Repeated Information": (
        "**Practice removing repetition.** Read each sentence and ask: 'Did I already say this idea?' "
        "If two sentences express the same point in different words, cut the one that adds less information. "
        "Every sentence should contribute something new."
    ),
    "Combining Sentences": (
        "**Practice sentence combining.** When you have two short sentences about the same action or idea, "
        "try combining them with a participial phrase (-ing or -ed), a subordinating conjunction "
        "(while, after, because, although), or a semicolon. Avoid repeating the subject unnecessarily."
    ),
    "Word Choice": (
        "**Practice improving word choice.** Replace vague or informal words (bad, good, nice, big, sad) "
        "with precise, specific language that fits the academic tone. "
        "Ask: Does this word exactly describe what I mean? Or is there a more specific word available?"
    ),
    "Sentence Fragments": (
        "**Practice identifying and fixing sentence fragments.** Check every sentence: "
        "Does it have a subject? Does it have a complete verb? "
        "Watch out for sentences starting with 'because,' 'although,' 'while,' 'since,' or 'if' — "
        "these are dependent clauses and cannot stand alone."
    ),
    "Run-On Sentences": (
        "**Practice fixing run-on sentences.** Two complete sentences cannot be joined without punctuation. "
        "Fix options: (1) Use a period and start a new sentence. "
        "(2) Use a semicolon between the two complete thoughts. "
        "(3) Add a conjunction (and, but, so, yet, for, or, nor). "
        "Remember: a comma alone is NOT enough — that creates a comma splice."
    ),
    "Verb Tense": (
        "**Practice verb tense consistency.** Look for time signal words: "
        "'yesterday,' 'in 1969,' 'last week' → past tense. "
        "'tomorrow,' 'next year,' 'will' → future tense. "
        "All verbs in a sentence describing the same event should use the same tense."
    ),
    "Subject-Verb Agreement": (
        "**Practice subject-verb agreement.** Find the main subject of the sentence — "
        "ignore prepositional phrases like 'of the students' or 'in the box.' "
        "Singular subjects (one person, one thing, a group acting as one) → singular verb (is, was, has). "
        "Plural subjects → plural verb (are, were, have)."
    ),
    "Capitalization": (
        "**Practice capitalization rules.** Capitalize: specific names of people, places, streets, "
        "schools, organizations, and titles used before a name (President Lincoln, Dr. Rivera). "
        "Do NOT capitalize: general nouns (a library, a museum, a president) or school subjects "
        "unless they are proper names (English, Spanish — but not history or science)."
    ),
    "Punctuation — Unnecessary Comma": (
        "**Practice punctuation and comma rules.** Never place a comma between a subject and its verb. "
        "Common correct comma uses: after an introductory phrase, between items in a list, "
        "before a coordinating conjunction (and, but, so) joining two complete sentences. "
        "When in doubt, read the sentence aloud — if the pause sounds wrong, the comma is probably wrong."
    ),
}

# ── Separate exercises by section ─────────────────────────────────────────────
revising_exercises = [ex for ex in EXERCISES if ex["section"] == "Revising"]
editing_exercises  = [ex for ex in EXERCISES if ex["section"] == "Editing"]

# ── Page header ───────────────────────────────────────────────────────────────
st.title("✏️ Revising and Editing Practice")
st.markdown(
    "This section has two parts — **Revising** and **Editing**. "
    "Each part tests different skills. Read the mini-lesson before each question."
)

col_rev, col_edit = st.columns(2)
col_rev.info("**Revising** improves *meaning*: claims, transitions, supporting details, word choice, sentence clarity, organization, and removing repetition.")
col_edit.info("**Editing** fixes *correctness*: grammar, punctuation, capitalization, spelling, fragments, run-ons, verb tense, and subject-verb agreement.")

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_rev, tab_edit = st.tabs(["📝 Revising Practice", "🔧 Editing Practice"])


def render_exercises(exercises, section_key, submitted_key, answers_key):
    """
    Render a set of exercises, submit button, and feedback for one section.
    section_key: short prefix used for widget keys ('rev' or 'edit')
    """
    if submitted_key not in st.session_state:
        st.session_state[submitted_key] = False
    if answers_key not in st.session_state:
        st.session_state[answers_key] = {}

    answers = {}
    for ex in exercises:
        st.divider()

        # Skill + TEKS tag
        difficulty_colors = {"Basic": "🟢", "Medium": "🟡", "Advanced": "🔴"}
        icon = difficulty_colors.get(ex["difficulty"], "⚪")
        st.markdown(
            f"**{icon} {ex['skill']}** &nbsp;|&nbsp; "
            f"<span style='font-size:0.8em; color:gray;'>{ex['teks']} · {ex['difficulty']}</span>",
            unsafe_allow_html=True,
        )

        # Mini-lesson rule
        st.info(f"📌 **Quick Rule:** {ex['rule']}")

        # Passage / sentence
        if ex["section"] == "Revising":
            st.markdown("**Read the following passage:**")
            st.markdown(ex["sentence"])
            st.markdown(f"**Question:** {ex['instruction']}")
        else:
            st.markdown(f"**{ex['instruction']}**")
            st.markdown(f"**Sentence:** {ex['sentence']}")

        # Answer choices
        answer = st.radio(
            label=f"Answer for Exercise {ex['id']}",
            options=ex["options"],
            index=None,
            key=f"{section_key}_{ex['id']}",
            label_visibility="collapsed",
            disabled=st.session_state[submitted_key],
        )
        answers[ex["id"]] = answer

    # Submit button
    st.divider()
    if not st.session_state[submitted_key]:
        if st.button("Submit Answers", type="primary", key=f"submit_{section_key}"):
            if None in answers.values():
                st.warning("Please answer all questions before submitting.")
            else:
                st.session_state[answers_key] = answers
                st.session_state[submitted_key] = True
                st.rerun()
        else:
            unanswered = sum(1 for v in answers.values() if v is None)
            if unanswered > 0:
                st.caption(f"{len(exercises) - unanswered}/{len(exercises)} questions answered")

    # ── Results ───────────────────────────────────────────────────────────────
    if st.session_state[submitted_key]:
        score = 0
        missed_skills = []

        for ex in exercises:
            user_answer    = st.session_state[answers_key].get(ex["id"])
            correct_answer = ex["options"][ex["correct"]]
            is_correct     = user_answer == correct_answer

            if is_correct:
                score += 1
                st.success(
                    f"✅ **Question {ex['id']} — {ex['skill']}:** Correct!"
                )
            else:
                missed_skills.append(ex["skill"])
                st.error(
                    f"❌ **Question {ex['id']} — {ex['skill']}:** Incorrect\n\n"
                    f"**Your answer:** {user_answer}\n\n"
                    f"**Correct answer:** {correct_answer}"
                )

            with st.expander(f"📖 Explanation — Question {ex['id']}"):
                st.markdown(f"**Rule reminder:** {ex['rule']}")
                st.markdown(f"**Why this answer is correct:** {ex['explanation']}")

        # Score summary
        st.divider()
        total      = len(exercises)
        percentage = int((score / total) * 100)
        st.metric(
            f"{exercises[0]['section']} Score",
            f"{score} / {total}",
            f"{percentage}%",
        )

        if percentage == 100:
            st.balloons()
            st.success("Perfect score! Excellent work.")
        elif percentage >= 80:
            st.success("Strong performance! Review the explanations above for any items you missed.")
        elif percentage >= 60:
            st.info("Good effort. Read the explanations carefully — the mini-lessons will help you remember the rules.")
        else:
            st.warning("Keep practicing. Focus on the recommendations below, then try again.")

        # Skill breakdown
        if missed_skills:
            st.divider()
            st.subheader("🎯 Skills to Practice")
            st.markdown("Based on your answers, focus on these areas:")

            shown = []
            for skill in missed_skills:
                if skill not in shown and skill in SKILL_RECOMMENDATIONS:
                    st.warning(SKILL_RECOMMENDATIONS[skill])
                    shown.append(skill)

        # Try Again button
        st.divider()
        if st.button("🔄 Try Again", key=f"retry_{section_key}"):
            st.session_state[submitted_key] = False
            st.session_state[answers_key]   = {}
            for ex in exercises:
                key = f"{section_key}_{ex['id']}"
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()


# ── Revising tab ──────────────────────────────────────────────────────────────
with tab_rev:
    st.markdown(
        "**Revising** means improving the meaning, organization, and development of a piece of writing. "
        "You are not looking for grammar errors — you are looking for ways to make the writing stronger and clearer."
    )
    render_exercises(
        revising_exercises,
        section_key="rev",
        submitted_key="revising_submitted",
        answers_key="revising_answers",
    )

# ── Editing tab ───────────────────────────────────────────────────────────────
with tab_edit:
    st.markdown(
        "**Editing** means correcting errors in grammar, punctuation, capitalization, spelling, and sentence structure. "
        "You are looking for mistakes in correctness — not improvements to meaning."
    )
    render_exercises(
        editing_exercises,
        section_key="edit",
        submitted_key="editing_submitted",
        answers_key="editing_answers",
    )
