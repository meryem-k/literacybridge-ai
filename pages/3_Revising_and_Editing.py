import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.revising_editing import EXERCISES

st.set_page_config(page_title="Revising & Editing", page_icon="✏️")

st.title("✏️ Revising and Editing Practice")
st.markdown("Practice fixing common grammar and punctuation errors — just like on the STAAR test.")

# Initialize session state
if "editing_submitted" not in st.session_state:
    st.session_state.editing_submitted = False
if "editing_answers" not in st.session_state:
    st.session_state.editing_answers = {}

# Show each exercise
answers = {}
for ex in EXERCISES:
    st.subheader(f"Exercise {ex['id']}: {ex['type']} — {ex['skill']}")
    st.markdown(ex["instruction"])
    st.markdown(f"**Sentence:** {ex['sentence']}")

    answer = st.radio(
        label=f"Answer for Exercise {ex['id']}",
        options=ex["options"],
        index=None,
        key=f"edit{ex['id']}",
        label_visibility="collapsed",
    )
    answers[ex["id"]] = answer
    st.markdown("")

# Submit button
if not st.session_state.editing_submitted:
    if st.button("Submit Answers", type="primary"):
        if None in answers.values():
            st.warning("Please answer all exercises before submitting.")
        else:
            st.session_state.editing_answers = answers
            st.session_state.editing_submitted = True
            st.rerun()

# --- Results Section ---
if st.session_state.editing_submitted:
    st.divider()
    st.subheader("Your Results")

    score = 0
    for ex in EXERCISES:
        user_answer = st.session_state.editing_answers.get(ex["id"])
        correct_answer = ex["options"][ex["correct"]]
        is_correct = user_answer == correct_answer

        if is_correct:
            score += 1
            st.success(f"✅ Exercise {ex['id']}: Correct!")
        else:
            st.error(f"❌ Exercise {ex['id']}: Incorrect — The correct answer is: **{correct_answer}**")

        with st.expander(f"See explanation for Exercise {ex['id']}"):
            st.write(ex["explanation"])

    st.divider()
    percentage = int((score / len(EXERCISES)) * 100)
    st.metric("Your Score", f"{score} / {len(EXERCISES)}", f"{percentage}%")

    if percentage == 100:
        st.balloons()
        st.success("Perfect! You know your grammar rules!")
    elif percentage >= 75:
        st.success("Great job! You are getting strong at revising and editing.")
    elif percentage >= 50:
        st.info("Good effort! Review the explanations above and try again.")
    else:
        st.warning("Keep practicing! Grammar takes time. Read each explanation carefully.")

    if st.button("Try Again"):
        st.session_state.editing_submitted = False
        st.session_state.editing_answers = {}
        for ex in EXERCISES:
            key = f"edit{ex['id']}"
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
