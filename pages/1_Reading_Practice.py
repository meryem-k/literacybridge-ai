import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.passages import PASSAGES

st.set_page_config(page_title="Reading Practice", page_icon="📖")

st.title("📖 Reading Practice")
st.markdown("Choose a passage, read it carefully, then answer the STAAR-style questions.")

# --- Passage Selector ---
passage_options = {f"{p['genre']}: \"{p['title']}\"": p for p in PASSAGES}
selected_label = st.selectbox("Select a passage to practice:", list(passage_options.keys()))
passage = passage_options[selected_label]

# Use passage id in session state keys so switching passages resets the quiz
pid = passage["id"]

st.divider()

# --- Reading Passage ---
with st.expander(f'📄 Read the passage: **"{passage["title"]}"**', expanded=True):
    st.caption(f"Genre: {passage['genre']}")
    st.markdown(passage["text"])

st.divider()
st.subheader("Answer the Questions")
st.caption("Choose the best answer for each question. Submit when you are finished.")

# Session state keys are passage-specific so switching resets everything cleanly
submitted_key = f"submitted_{pid}"
answers_key   = f"answers_{pid}"

if submitted_key not in st.session_state:
    st.session_state[submitted_key] = False
if answers_key not in st.session_state:
    st.session_state[answers_key] = {}

# --- Questions ---
answers = {}
for q in passage["questions"]:
    st.markdown(f"**Question {q['id']}** — *{q['skill']}*")
    st.markdown(f"**{q['question']}**")
    answer = st.radio(
        label=f"Answer for Question {q['id']}",
        options=q["options"],
        index=None,
        key=f"p{pid}_q{q['id']}",
        label_visibility="collapsed",
    )
    answers[q["id"]] = answer
    st.markdown("")

# --- Submit ---
if not st.session_state[submitted_key]:
    if st.button("Submit Answers", type="primary"):
        if None in answers.values():
            st.warning("Please answer all questions before submitting.")
        else:
            st.session_state[answers_key] = answers
            st.session_state[submitted_key] = True
            st.rerun()

# --- Results ---
if st.session_state[submitted_key]:
    st.divider()
    st.subheader("Your Results")

    score = 0
    for q in passage["questions"]:
        user_answer    = st.session_state[answers_key].get(q["id"])
        correct_answer = q["options"][q["correct"]]
        is_correct     = user_answer == correct_answer

        if is_correct:
            score += 1
            st.success(f"✅ Question {q['id']}: Correct!  |  *{q['skill']}*")
        else:
            st.error(f"❌ Question {q['id']}: Incorrect  |  *{q['skill']}*\n\n**Correct answer:** {correct_answer}")

        with st.expander(f"See explanation for Question {q['id']}"):
            st.write(q["explanation"])

    st.divider()
    total      = len(passage["questions"])
    percentage = int((score / total) * 100)
    st.metric("Your Score", f"{score} / {total}", f"{percentage}%")

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
        st.session_state[submitted_key] = False
        st.session_state[answers_key]   = {}
        for q in passage["questions"]:
            key = f"p{pid}_q{q['id']}"
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()
