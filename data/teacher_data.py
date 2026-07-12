STUDENTS = [
    {"name": "Sofia Martinez",   "reading": 78, "vocabulary": 82, "writing": 75, "revising": 70},
    {"name": "James Johnson",    "reading": 85, "vocabulary": 88, "writing": 90, "revising": 85},
    {"name": "Linh Nguyen",      "reading": 72, "vocabulary": 68, "writing": 65, "revising": 70},
    {"name": "Marco Hernandez",  "reading": 65, "vocabulary": 70, "writing": 60, "revising": 58},
    {"name": "Aisha Williams",   "reading": 90, "vocabulary": 92, "writing": 88, "revising": 91},
    {"name": "David Kim",        "reading": 80, "vocabulary": 75, "writing": 72, "revising": 78},
    {"name": "Maria Rodriguez",  "reading": 68, "vocabulary": 65, "writing": 62, "revising": 60},
    {"name": "Jamal Thompson",   "reading": 77, "vocabulary": 80, "writing": 74, "revising": 76},
    {"name": "Yuki Tanaka",      "reading": 88, "vocabulary": 85, "writing": 83, "revising": 86},
    {"name": "Carlos Santos",    "reading": 62, "vocabulary": 58, "writing": 55, "revising": 60},
]

WEEKLY_PROGRESS = {
    "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "Reading":             [65, 68, 72, 75],
    "Vocabulary":          [60, 65, 70, 73],
    "Writing":             [58, 62, 66, 70],
    "Revising & Editing":  [55, 60, 64, 68],
}

WRITING_SKILL_LABELS = [
    "Answering the Prompt",
    "Citing Evidence",
    "Explaining Evidence",
    "Grammar & Sentence Clarity",
    "Organization",
    "Connecting Back",
]

# Per-student scores for each writing skill (sample data, 0–100)
STUDENT_WRITING_SKILLS = [
    {"name": "Sofia Martinez",  "Answering the Prompt": 78, "Citing Evidence": 52, "Explaining Evidence": 42, "Grammar & Sentence Clarity": 72, "Organization": 62, "Connecting Back": 40},
    {"name": "James Johnson",   "Answering the Prompt": 90, "Citing Evidence": 82, "Explaining Evidence": 78, "Grammar & Sentence Clarity": 88, "Organization": 80, "Connecting Back": 75},
    {"name": "Linh Nguyen",     "Answering the Prompt": 72, "Citing Evidence": 48, "Explaining Evidence": 40, "Grammar & Sentence Clarity": 62, "Organization": 60, "Connecting Back": 45},
    {"name": "Marco Hernandez", "Answering the Prompt": 58, "Citing Evidence": 40, "Explaining Evidence": 32, "Grammar & Sentence Clarity": 50, "Organization": 44, "Connecting Back": 30},
    {"name": "Aisha Williams",  "Answering the Prompt": 92, "Citing Evidence": 88, "Explaining Evidence": 85, "Grammar & Sentence Clarity": 90, "Organization": 86, "Connecting Back": 82},
    {"name": "David Kim",       "Answering the Prompt": 82, "Citing Evidence": 68, "Explaining Evidence": 60, "Grammar & Sentence Clarity": 80, "Organization": 70, "Connecting Back": 46},
    {"name": "Maria Rodriguez", "Answering the Prompt": 65, "Citing Evidence": 38, "Explaining Evidence": 30, "Grammar & Sentence Clarity": 60, "Organization": 48, "Connecting Back": 28},
    {"name": "Jamal Thompson",  "Answering the Prompt": 78, "Citing Evidence": 70, "Explaining Evidence": 62, "Grammar & Sentence Clarity": 74, "Organization": 65, "Connecting Back": 52},
    {"name": "Yuki Tanaka",     "Answering the Prompt": 88, "Citing Evidence": 80, "Explaining Evidence": 75, "Grammar & Sentence Clarity": 84, "Organization": 78, "Connecting Back": 70},
    {"name": "Carlos Santos",   "Answering the Prompt": 50, "Citing Evidence": 28, "Explaining Evidence": 22, "Grammar & Sentence Clarity": 42, "Organization": 35, "Connecting Back": 20},
]

REVISING_SKILL_LABELS = [
    "Strengthening Claims",
    "Transitions",
    "Adding Supporting Details",
    "Removing Repetition",
    "Combining Sentences",
    "Word Choice",
]

EDITING_SKILL_LABELS = [
    "Sentence Fragments",
    "Run-On Sentences",
    "Verb Tense",
    "Subject-Verb Agreement",
    "Capitalization",
    "Punctuation",
]

# Per-student revising and editing skill scores (sample data, 0–100)
STUDENT_REVISING_EDITING_SKILLS = [
    {"name": "Sofia Martinez",  "Strengthening Claims": 72, "Transitions": 68, "Adding Supporting Details": 60, "Removing Repetition": 75, "Combining Sentences": 55, "Word Choice": 70, "Sentence Fragments": 85, "Run-On Sentences": 78, "Verb Tense": 72, "Subject-Verb Agreement": 80, "Capitalization": 88, "Punctuation": 65},
    {"name": "James Johnson",   "Strengthening Claims": 88, "Transitions": 85, "Adding Supporting Details": 82, "Removing Repetition": 90, "Combining Sentences": 80, "Word Choice": 85, "Sentence Fragments": 92, "Run-On Sentences": 90, "Verb Tense": 88, "Subject-Verb Agreement": 90, "Capitalization": 92, "Punctuation": 88},
    {"name": "Linh Nguyen",     "Strengthening Claims": 60, "Transitions": 52, "Adding Supporting Details": 55, "Removing Repetition": 68, "Combining Sentences": 48, "Word Choice": 62, "Sentence Fragments": 75, "Run-On Sentences": 70, "Verb Tense": 65, "Subject-Verb Agreement": 72, "Capitalization": 80, "Punctuation": 60},
    {"name": "Marco Hernandez", "Strengthening Claims": 45, "Transitions": 40, "Adding Supporting Details": 42, "Removing Repetition": 58, "Combining Sentences": 35, "Word Choice": 50, "Sentence Fragments": 65, "Run-On Sentences": 58, "Verb Tense": 50, "Subject-Verb Agreement": 60, "Capitalization": 70, "Punctuation": 48},
    {"name": "Aisha Williams",  "Strengthening Claims": 90, "Transitions": 88, "Adding Supporting Details": 85, "Removing Repetition": 92, "Combining Sentences": 82, "Word Choice": 88, "Sentence Fragments": 95, "Run-On Sentences": 92, "Verb Tense": 90, "Subject-Verb Agreement": 92, "Capitalization": 95, "Punctuation": 90},
    {"name": "David Kim",       "Strengthening Claims": 75, "Transitions": 70, "Adding Supporting Details": 72, "Removing Repetition": 80, "Combining Sentences": 65, "Word Choice": 75, "Sentence Fragments": 82, "Run-On Sentences": 78, "Verb Tense": 70, "Subject-Verb Agreement": 78, "Capitalization": 85, "Punctuation": 72},
    {"name": "Maria Rodriguez", "Strengthening Claims": 50, "Transitions": 45, "Adding Supporting Details": 48, "Removing Repetition": 62, "Combining Sentences": 38, "Word Choice": 55, "Sentence Fragments": 68, "Run-On Sentences": 62, "Verb Tense": 55, "Subject-Verb Agreement": 65, "Capitalization": 72, "Punctuation": 52},
    {"name": "Jamal Thompson",  "Strengthening Claims": 78, "Transitions": 72, "Adding Supporting Details": 75, "Removing Repetition": 82, "Combining Sentences": 68, "Word Choice": 78, "Sentence Fragments": 85, "Run-On Sentences": 80, "Verb Tense": 75, "Subject-Verb Agreement": 82, "Capitalization": 88, "Punctuation": 74},
    {"name": "Yuki Tanaka",     "Strengthening Claims": 85, "Transitions": 82, "Adding Supporting Details": 80, "Removing Repetition": 88, "Combining Sentences": 78, "Word Choice": 82, "Sentence Fragments": 90, "Run-On Sentences": 88, "Verb Tense": 84, "Subject-Verb Agreement": 88, "Capitalization": 92, "Punctuation": 85},
    {"name": "Carlos Santos",   "Strengthening Claims": 38, "Transitions": 32, "Adding Supporting Details": 35, "Removing Repetition": 48, "Combining Sentences": 28, "Word Choice": 42, "Sentence Fragments": 58, "Run-On Sentences": 50, "Verb Tense": 42, "Subject-Verb Agreement": 52, "Capitalization": 62, "Punctuation": 40},
]

# Class-level revising and editing skill percentages (sample data)
REVISING_EDITING_CLASS_SAMPLE = {
    "Skill": [
        "Strengthening Claims", "Transitions", "Adding Supporting Details",
        "Removing Repetition", "Combining Sentences", "Word Choice",
        "Sentence Fragments", "Run-On Sentences", "Verb Tense",
        "Subject-Verb Agreement", "Capitalization", "Punctuation",
    ],
    "Section": ["Revising"] * 6 + ["Editing"] * 6,
    "Students Showing Skill (%)": [
        68, 63, 63, 74, 58, 69,   # Revising
        80, 75, 69, 76, 82, 67,   # Editing
    ],
}

WRITING_SKILL_SAMPLE = {
    "Skill": [
        "Answering the Prompt",
        "Citing Evidence",
        "Explaining Evidence",
        "Organization",
        "Sentence Clarity",
        "Grammar",
    ],
    "Students Showing Skill (%)": [74, 55, 42, 49, 60, 65],
}
