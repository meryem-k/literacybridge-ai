import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.passages import PASSAGE

st.set_page_config(page_title="Reading Practice", page_icon="📖")

st.title("📖 Reading Practice")
st.markdown("Read the passage carefully. Then answer the questions below.")

# --- Reading Passage ---
with st.expander(f'📄 Click to read the passage: **"{PASSAGE["title"]}"**', expanded=True):
    st.markdown(PASSAGE["text"])

st.divider()
st.subheader("Answer the Questions")
st.caption("Choose the best answer for each question. Submit when you are finished.")

# Initialize session state to remember answers and whether the student submitted
if "reading_submitted" not in st.session_state:
    st.session_state.reading_submitted = False
if "reading_answers" not in st.session_state:
    st.session_state.reading_answers = {}

# Show each question with radio buttons
answers = {}
for q in PASSAGE["questions"]:
    st.markdown(f"**Question {q['id']}:** {q['question']}")
    answer = st.radio(
        label=f"Answer for Question {q['id']}",
        options=q["options"],
        index=None,
        key=f"q{q['id']}",
        label_visibility="collapsed",
    )
    answers[q["id"]] = answer
    st.markdown("")

# Submit button — only show if not yet submitted
if not st.session_state.reading_submitted:
    if st.button("Submit Answers", type="primary"):
        if None in answers.values():
            st.warning("Please answer all questions before submitting.")
        else:
            st.session_state.reading_answers = answers
            st.session_state.reading_submitted = True
            st.rerun()

# --- Results Section ---
if st.session_state.reading_submitted:
    st.divider()
    st.subheader("Your Results")

    score = 0
    for q in PASSAGE["questions"]:
        user_answer = st.session_state.reading_answers.get(q["id"])
        correct_answer = q["options"][q["correct"]]
        is_correct = user_answer == correct_answer

        if is_correct:
            score += 1
            st.success(f"✅ Question {q['id']}: Correct!")
        else:
            st.error(f"❌ Question {q['id']}: Incorrect — The correct answer is: **{correct_answer}**")

        with st.expander(f"See explanation for Question {q['id']}"):
            st.write(q["explanation"])

    st.divider()
    percentage = int((score / len(PASSAGE["questions"])) * 100)
    st.metric("Your Score", f"{score} / {len(PASSAGE['questions'])}", f"{percentage}%")

    if percentage == 100:
        st.balloons()
        st.success("Perfect score! Excellent work!")
    elif percentage >= 80:
        st.success("Great job! Keep it up!")
    elif percentage >= 60:
        st.info("Good effort! Review the explanations above and try again.")
    else:
        st.warning("Keep practicing! Read the explanations carefully and ask your teacher for help.")

    if st.button("Try Again"):
        st.session_state.reading_submitted = False
        st.session_state.reading_answers = {}
        for q in PASSAGE["questions"]:
            key = f"q{q['id']}"
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
