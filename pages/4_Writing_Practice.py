import streamlit as st

st.set_page_config(page_title="Writing Practice", page_icon="🖊️")

st.title("🖊️ Short-Constructed Response Writing")
st.markdown("Practice writing a short-constructed response (SCR) using the ACE or RACE framework.")

# --- Writing Prompt ---
st.subheader("Writing Prompt")
st.info("""
Based on the passage **"Finding Words,"** answer the following question in 3–5 sentences:

**How does the author show that Marisol is determined to learn English? Use evidence from the text to support your answer.**
""")

# --- Framework Guide ---
st.subheader("Choose Your Writing Framework")
st.markdown("Pick the framework your teacher has assigned, or choose the one that feels most comfortable.")

tab_ace, tab_race = st.tabs(["ACE Framework", "RACE Framework"])

with tab_ace:
    st.markdown("""
**A — Answer** the question directly in your first sentence.
**C — Cite** evidence from the text (use a direct quote or a specific detail).
**E — Explain** how your evidence supports your answer.

> **Starter sentences to get you going:**
> - *A:* "The author shows Marisol's determination by..."
> - *C:* "For example, the text states, '...'"
> - *E:* "This shows that Marisol..."
""")

with tab_race:
    st.markdown("""
**R — Restate** the question in your own words as your first sentence.
**A — Answer** the question directly.
**C — Cite** evidence from the text (use a direct quote or a specific detail).
**E — Explain** how your evidence supports your answer.

> **Starter sentences to get you going:**
> - *R:* "The author uses several details to show Marisol's determination."
> - *A:* "Marisol is clearly motivated to learn English because..."
> - *C:* "The passage states, '...'"
> - *E:* "This proves that..."
""")

# --- Text Area ---
st.subheader("Your Response")
response = st.text_area(
    "Type your short-constructed response here:",
    height=200,
    placeholder="Start writing your response here...",
    key="scr_response",
)

word_count = len(response.split()) if response.strip() else 0
st.caption(f"Word count: {word_count}")

# --- Self-Assessment Checklist ---
st.subheader("Self-Assessment Checklist")
st.markdown("Check each box when you are satisfied that your response meets that requirement:")

check1 = st.checkbox("I answered the question directly in my first sentence.")
check2 = st.checkbox("I included a quote or specific detail from the text.")
check3 = st.checkbox("I explained how my evidence connects to my answer.")
check4 = st.checkbox("I used complete sentences.")
check5 = st.checkbox("I checked for spelling and grammar errors.")

checks_done = sum([check1, check2, check3, check4, check5])

# --- Submit and Feedback ---
if response.strip():
    if st.button("Submit My Response", type="primary"):
        st.divider()
        st.subheader("Feedback on Your Response")

        # Length feedback
        if word_count < 30:
            st.warning("⚠️ Your response seems short. Try to write at least 3 complete sentences.")
        elif word_count >= 50:
            st.success("✅ Good length! Your response has enough detail.")
        else:
            st.info("📏 Your response is a good start. Consider adding more explanation.")

        # Evidence feedback
        has_quote = '"' in response
        if has_quote:
            st.success("✅ Great! It looks like you included a direct quote from the passage.")
        else:
            st.info('💡 Tip: Try including a direct quote from the passage using quotation marks (" ").')

        # Transition words feedback
        transition_phrases = [
            "for example", "the text states", "according to", "the passage",
            "this shows", "this demonstrates", "therefore", "in the passage",
        ]
        has_transition = any(phrase in response.lower() for phrase in transition_phrases)
        if has_transition:
            st.success("✅ Nice! You used text-referencing language in your response.")
        else:
            st.info('💡 Tip: Use phrases like "For example," or "The text states," to introduce your evidence.')

        # Checklist feedback
        if checks_done == 5:
            st.success("✅ Excellent! You completed all self-assessment checks.")
        else:
            st.info(f"You completed {checks_done} out of 5 self-assessment checks. Review the unchecked items.")

        st.markdown("---")
        st.markdown("**Your response has been recorded.** In a future version, your teacher will be able to view and give feedback on your writing.")
else:
    st.caption("Type your response above, then click Submit.")
