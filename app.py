import streamlit as st

st.set_page_config(
    page_title="Literacy Bridge AI",
    page_icon="📚",
    layout="centered",
)

st.title("📚 Literacy Bridge AI")
st.subheader("English Literacy Support for High School Students")

st.markdown("""
Welcome to **Literacy Bridge AI** — a learning tool designed to help you build strong English skills for the STAAR test and beyond.

---

### What Can You Do Here?

| Page | What You Will Practice |
|------|------------------------|
| 📖 **Reading Practice** | Read a STAAR-style passage and answer comprehension questions |
| 📝 **Vocabulary Support** | Learn key academic vocabulary with definitions and examples |
| ✏️ **Revising & Editing** | Fix grammar and punctuation errors — just like on the STAAR test |
| 🖊️ **Writing Practice** | Write a short-constructed response using ACE or RACE |
| 📊 **Teacher Dashboard** | View sample student progress data *(teacher view)* |

---

### How to Get Started

Use the **menu on the left side** to choose any section.
You can go back and forth between pages anytime.

---
""")

st.info("💡 **Tip for students:** Start with Reading Practice, then try Vocabulary Support. These will help you prepare for the Writing activities.")

st.markdown("---")
st.caption("Literacy Bridge AI — Prototype v1.0 | Built for Harmony Charter School, English I")
