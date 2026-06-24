# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Literacy Bridge AI is an educational technology prototype that helps underserved, multilingual, immigrant, and academically at-risk 9th-grade students improve English literacy skills. It is built for an English I class at Harmony Charter School in Texas.

The developer is a high school English teacher — not a software engineer. **Keep all code simple, readable, and free of unnecessary abstraction.** Explain what you are going to do before running commands.

Target skill areas: STAAR-style reading comprehension, academic vocabulary, revising and editing, short-constructed response (SCR) writing using ACE/RACE, and teacher progress monitoring.

## Prototype Constraints (v1.0)

- **No database** — all content lives in `data/` as plain Python dictionaries
- **No login or authentication**
- **No external API calls** — everything runs locally
- **No paid services** — runs entirely on the user's machine

## Development Commands

```bash
# First time only — install dependencies
pip install -r requirements.txt

# Run the app (opens in browser at http://localhost:8501)
streamlit run app.py
```

## Architecture

This is a Streamlit multi-page app. Streamlit automatically turns files in `pages/` into sidebar navigation links. Numbers in filenames control the display order. Underscores become spaces in the sidebar label.

```
literacybridge-ai/
├── app.py                          # Homepage — Streamlit entry point
├── requirements.txt                # streamlit, pandas, plotly
├── data/                           # All hardcoded sample content
│   ├── passages.py                 # Reading passage + 5 STAAR-style questions
│   ├── vocabulary.py               # 10 academic vocabulary words
│   ├── revising_editing.py         # 4 grammar/punctuation exercises
│   └── teacher_data.py             # Sample student scores + weekly progress
└── pages/                          # One file per app section
    ├── 1_Reading_Practice.py       # Passage display + MCQ quiz with feedback
    ├── 2_Vocabulary_Support.py     # Vocab cards + full reference table
    ├── 3_Revising_and_Editing.py   # Grammar exercise quiz with feedback
    ├── 4_Writing_Practice.py       # SCR prompt + ACE/RACE guide + text input
    └── 5_Teacher_Dashboard.py      # Charts and student table (sample data only)
```

**Key Streamlit behavior:** The entire script reruns on every user interaction. Use `st.session_state` (a dictionary) to preserve answers and submission status across reruns — quiz answers, whether a student has submitted, etc.

**Data import pattern:** Each page file in `pages/` must add the project root to `sys.path` before importing from `data/`:

```python
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.passages import PASSAGE
```

## Adding New Content

**New reading passage:** Edit `data/passages.py`. Each passage is a dictionary with `title`, `text`, and a `questions` list. Each question needs `id`, `question`, `options` (list of 4 strings), `correct` (the index of the right answer, 0–3), and `explanation`.

**New vocabulary words:** Append a dictionary to `VOCABULARY_WORDS` in `data/vocabulary.py` with keys: `word`, `part_of_speech`, `definition`, `example`, `tip`.

**New editing exercises:** Append a dictionary to `EXERCISES` in `data/revising_editing.py` with keys: `id`, `type`, `skill`, `instruction`, `sentence`, `options`, `correct` (index), `explanation`.

## Coding Style

- Plain, readable Python — no classes, decorators, or complex patterns
- Use `st.success()`, `st.info()`, `st.warning()`, `st.error()` for colored feedback
- Student-facing text should be encouraging and use clear language
- Use STAAR test terminology: "central idea" (not "main idea"), "explicit/implicit," "text evidence," "short-constructed response"

## Git and GitHub Workflow

Always protect completed work by committing frequently and pushing to GitHub. Do not let progress accumulate without saving it.

### Commit After Every Meaningful Step

After completing any of the following, check Git status and create a commit:
- Adding or finishing a new page
- Adding new sample data (passage, vocabulary words, exercises)
- Fixing a bug or correcting an error
- Improving the layout or wording of a page
- Updating CLAUDE.md or requirements.txt

Do not bundle many unrelated changes into one large commit. Group related changes together and commit them as a unit.

### How to Check Status and Commit

Run these commands in the terminal from the project folder:

```bash
# See what files have changed
git status

# Stage all changed files
git add .

# Create a commit with a clear message
git commit -m "add reading practice page"
```

### Commit Message Style

Use short, lowercase messages that describe what was added or changed:

```
add Streamlit app structure
add reading practice page
add vocabulary support page
add teacher dashboard sample data
fix navigation bug
improve writing practice layout
update CLAUDE.md with Git workflow
```

Before committing, briefly describe what changed in plain English — for example: "I just finished the vocabulary page, so I will commit that now."

### Pushing to GitHub

Once a remote repository is connected, push after every commit:

```bash
git push
```

### Connecting to GitHub for the First Time

If GitHub is not yet connected, follow these steps once:

1. Go to github.com and create a new repository named `literacybridge-ai`. Leave it empty (no README).
2. Run these commands in the terminal (replace `YOUR_USERNAME` with your GitHub username):

```bash
git remote add origin https://github.com/YOUR_USERNAME/literacybridge-ai.git
git branch -M main
git push -u origin main
```

After this one-time setup, `git push` is all you need going forward.

### End-of-Session Reminder

At the end of every work session, check for uncommitted changes:

```bash
git status
```

If any files are listed, commit and push before closing the terminal. Never leave a session with unsaved, uncommitted work.

### Safety Rules

- Never delete a project file or overwrite important work without explaining what will be removed and why first.
- If a change is experimental or risky, describe it before making it and confirm with the user.

## Future Development Priorities

When ready to grow beyond this prototype:
1. Add more reading passages (mix of literary and informational texts)
2. Integrate Claude API for personalized writing feedback
3. Add SQLite database so student responses are saved
4. Add student login so progress is tracked per student
5. Expand teacher dashboard with real data from the database
