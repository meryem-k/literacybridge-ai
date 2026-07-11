# Literacy Bridge AI

**A personalized English literacy support tool for high school students**

---

## About This Project

Literacy Bridge AI is an educational technology prototype designed to help high school students build English literacy skills — with a particular focus on students who face additional barriers to academic success, including multilingual learners, immigrant students, English Language Learners, and students from low-income or working-class backgrounds.

The project was created by a practicing high school English I teacher in Texas as both a classroom support tool and a prototype for a broader educational technology vision: a platform that gives every student a personalized, guided path to English literacy improvement.

---

## Who It Is For

This tool is designed with the following students in mind:

- **Multilingual learners and English Language Learners** who are developing academic English while preparing for grade-level assessments
- **Immigrant students** who may have experienced interrupted schooling and need scaffolded support
- **Low-income and working-class students** who have limited access to tutoring or test preparation resources
- **Academically at-risk students** who benefit from structured, step-by-step guidance rather than open-ended study

---

## Current Features (Prototype v1.0)

The current prototype is a working Streamlit web application with five sections:

| Section | What Students Practice |
|---------|----------------------|
| Reading Practice | Three original STAAR-style passages with comprehension questions, skill labels, and answer explanations |
| Vocabulary Support | 20 academic vocabulary words organized into two sets, with definitions, example sentences, and study tips |
| Revising & Editing | Eight grammar and punctuation exercises covering subject-verb agreement, comma splices, apostrophes, verb tense, irrelevant information, thesis writing, capitalization, and pronoun case |
| Writing Practice | Short-constructed response (SCR) scaffolding using the ACE and RACE frameworks, with sentence stems, a sample labeled response, a student writing text box, and a self-assessment checklist. After submission: strengths-first feedback, personalized recommendations in ACE/RACE order, grammar and punctuation error detection with explanations, a "Next Best Step" prompt, and a "Try Revising Like This" example built from the student's own sentence. |
| Teacher Dashboard | Sample class overview metrics, skill-area charts, and a student progress table |

All content is aligned to Texas English I STAAR EOC standards and created by the teacher-developer. No content is copied from commercial test preparation materials.

---

## Vision: Personalized Literacy Intervention

The long-term goal of Literacy Bridge AI is to move beyond static practice toward **adaptive, personalized literacy support** — a system that responds to each student's specific learning needs rather than delivering the same content to everyone.

The platform is intended to eventually:

- Collect student performance data by skill area and text type
- Identify individual learning gaps in reading comprehension, grammar, vocabulary, revising, editing, and written expression
- Recommend targeted practice activities based on each student's areas of weakness
- Provide scaffolded explanations, sentence stems, and additional support for struggling students
- Track student improvement over time and make progress visible to both students and teachers
- Help teachers identify small groups of students with similar skill gaps for targeted mini-lessons
- Give students a clear, guided learning path — reducing the burden of figuring out what to study next

This vision is inspired by the principles of adaptive learning and formative assessment. The goal is to create a tool where students receive meaningful support at the moment they need it most — not after the test is over.

---

## Technology

- **Language:** Python 3.12
- **Interface:** [Streamlit](https://streamlit.io)
- **Data:** Local Python files (no database in current prototype)
- **Charts:** Plotly
- **Authentication:** None (prototype stage)

---

## Running Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

---

## Project Status

This is an active prototype under development. It is not yet a production system. Features, content, and design are evolving as the project grows toward its full vision.

**Phase 1 complete:** Content depth — three original STAAR-style passages, 20 academic vocabulary words, eight revising and editing exercises

**Phase 2 complete:** Writing practice improvements, including:
- ACE/RACE writing framework support with plain-English explanations and sentence stems
- Student writing text box with live word count
- Self-assessment checklist before submission
- Strengths-first feedback that recognizes what the student did well before listing gaps
- Personalized writing recommendations delivered in ACE/RACE order (Answer → Cite → Explain → Connect)
- Grammar and punctuation detection with explanations of why each error matters
- "Next Best Step" guidance — one clear action for the student to take
- "Try Revising Like This" support — a corrected example built from the student's own sentence
- Sample writing skill data added to the Teacher Dashboard for class-level insight

**Next phase:** Phase 3 — teacher usefulness (skill gap analysis, exportable reports, teacher guide page)

---

## Author

Developed by a high school English I teacher at Harmony Charter School in Texas.
Built to serve students. Designed to grow.
