import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.vocabulary import VOCABULARY_WORDS

st.set_page_config(page_title="Vocabulary Support", page_icon="📝")

st.title("📝 Vocabulary Support")
st.markdown("These are key academic words you will see on the STAAR test and in your reading assignments.")

# --- Set Filter ---
set_choice = st.radio(
    "Choose a word set:",
    ["Set 1 — Analysis & Reading Skills", "Set 2 — Literary & Argumentative Skills", "All Words"],
    horizontal=True,
)

if "Set 1" in set_choice:
    word_list = [w for w in VOCABULARY_WORDS if w["set"] == 1]
elif "Set 2" in set_choice:
    word_list = [w for w in VOCABULARY_WORDS if w["set"] == 2]
else:
    word_list = VOCABULARY_WORDS

# --- Word Selector ---
word_names = [w["word"] for w in word_list]

if not word_names:
    st.warning("No words found for this selection.")
    st.stop()

selected_word = st.selectbox("Choose a vocabulary word to study:", word_names)
word_data = next(w for w in word_list if w["word"] == selected_word)

st.divider()

# --- Word Card ---
col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown(f"## {word_data['word'].capitalize()}")
    st.caption(f"*{word_data['part_of_speech']}*")
    st.caption(f"Set {word_data['set']}")

with col_right:
    st.markdown("**Definition:**")
    st.markdown(word_data["definition"])

    st.markdown("**Example Sentence:**")
    st.markdown(f"> *{word_data['example']}*")

    st.markdown("**Study Tip:**")
    st.info(word_data["tip"])

st.divider()

# --- Full Reference Table ---
with st.expander(f"📋 View All Words in This Set ({len(word_list)} words)"):
    for w in word_list:
        st.markdown(f"**{w['word']}** *({w['part_of_speech']})* — {w['definition']}")

st.markdown("---")
st.info("💡 **Study Tip:** Try writing your own sentence using each vocabulary word. Writing it down helps you remember it.")
