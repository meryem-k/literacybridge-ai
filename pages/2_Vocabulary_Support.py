import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.vocabulary import VOCABULARY_WORDS

st.set_page_config(page_title="Vocabulary Support", page_icon="📝")

st.title("📝 Vocabulary Support")
st.markdown("These are key academic words you will see on the STAAR test and in your reading assignments.")

# Word selector
word_names = [w["word"] for w in VOCABULARY_WORDS]
selected_word = st.selectbox("Choose a vocabulary word to study:", word_names)

# Find the selected word's data
word_data = next(w for w in VOCABULARY_WORDS if w["word"] == selected_word)

st.divider()

col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown(f"## {word_data['word'].capitalize()}")
    st.caption(f"*{word_data['part_of_speech']}*")

with col_right:
    st.markdown("**Definition:**")
    st.markdown(word_data["definition"])

    st.markdown("**Example Sentence:**")
    st.markdown(f"> *{word_data['example']}*")

    st.markdown("**Study Tip:**")
    st.info(word_data["tip"])

st.divider()

# Full reference table
with st.expander("📋 View All Vocabulary Words at Once"):
    for w in VOCABULARY_WORDS:
        st.markdown(f"**{w['word']}** *({w['part_of_speech']})* — {w['definition']}")

st.markdown("---")
st.info("💡 **Study Tip:** Try writing your own sentence using each vocabulary word. Writing it down helps you remember it.")
