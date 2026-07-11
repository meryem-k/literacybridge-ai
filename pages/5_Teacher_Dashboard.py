import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.teacher_data import (
    STUDENTS, WEEKLY_PROGRESS, WRITING_SKILL_SAMPLE,
    WRITING_SKILL_LABELS, STUDENT_WRITING_SKILLS,
)

st.set_page_config(page_title="Teacher Dashboard", page_icon="📊", layout="wide")

st.title("📊 Teacher Dashboard")
st.warning("⚠️ This page shows **sample/demo data only**. No real student data is stored in this prototype.")

# Build a DataFrame from the sample student list
df = pd.DataFrame(STUDENTS)
df["Average"] = df[["reading", "vocabulary", "writing", "revising"]].mean(axis=1).round(1)

# --- Class Overview Metrics ---
st.subheader("Class Overview")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg. Reading Score",    f"{df['reading'].mean():.0f}%")
col2.metric("Avg. Vocabulary Score", f"{df['vocabulary'].mean():.0f}%")
col3.metric("Avg. Writing Score",    f"{df['writing'].mean():.0f}%")
col4.metric("Avg. Revising Score",   f"{df['revising'].mean():.0f}%")

st.divider()

# --- Charts ---
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Class Average by Skill")
    skill_avg = {
        "Skill": ["Reading", "Vocabulary", "Writing", "Revising & Editing"],
        "Average Score": [
            df["reading"].mean(),
            df["vocabulary"].mean(),
            df["writing"].mean(),
            df["revising"].mean(),
        ],
    }
    fig_bar = px.bar(
        skill_avg,
        x="Skill",
        y="Average Score",
        color="Skill",
        title="Average Scores by Skill Area",
        range_y=[0, 100],
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    fig_bar.update_layout(showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    st.subheader("Progress Over 4 Weeks")
    progress_df = pd.DataFrame(WEEKLY_PROGRESS)
    melted = progress_df.melt(id_vars="Week", var_name="Skill", value_name="Score")
    fig_line = px.line(
        melted,
        x="Week",
        y="Score",
        color="Skill",
        title="Weekly Class Progress by Skill",
        markers=True,
        range_y=[0, 100],
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# --- Individual Student Scores Table ---
st.subheader("Individual Student Scores")
display_df = df.rename(columns={
    "name":     "Student Name",
    "reading":  "Reading (%)",
    "vocabulary": "Vocabulary (%)",
    "writing":  "Writing (%)",
    "revising": "Revising (%)",
    "Average":  "Average (%)",
})
st.dataframe(display_df, use_container_width=True, hide_index=True)

st.divider()

# --- Students Who May Need Support ---
st.subheader("Students Who May Need Additional Support (Average below 70%)")
struggling = df[df["Average"] < 70].copy()

if struggling.empty:
    st.success("All students are currently at or above 70% average.")
else:
    struggling_display = struggling.rename(columns={
        "name":     "Student Name",
        "reading":  "Reading (%)",
        "vocabulary": "Vocabulary (%)",
        "writing":  "Writing (%)",
        "revising": "Revising (%)",
        "Average":  "Average (%)",
    })
    st.dataframe(struggling_display, use_container_width=True, hide_index=True)
    st.caption(f"{len(struggling)} student(s) may benefit from additional support or intervention.")

st.divider()

# --- Writing Skill Gap Analysis ---
st.subheader("Writing Skill Gap Analysis")
st.caption(
    "Percentage of students demonstrating each SCR writing skill "
    "based on recent Writing Practice submissions (sample data)."
)

writing_df = pd.DataFrame(WRITING_SKILL_SAMPLE)
fig_writing = px.bar(
    writing_df,
    x="Skill",
    y="Students Showing Skill (%)",
    color="Students Showing Skill (%)",
    title="Class Writing Skills — Students Showing Evidence of Each Skill",
    range_y=[0, 100],
    color_continuous_scale=["#d73027", "#fee08b", "#1a9850"],
    color_continuous_midpoint=65,
)
fig_writing.update_layout(
    showlegend=False,
    coloraxis_showscale=False,
    xaxis_tickangle=-20,
)
fig_writing.add_hline(
    y=70,
    line_dash="dash",
    line_color="gray",
    annotation_text="Target: 70%",
    annotation_position="top right",
)
st.plotly_chart(fig_writing, use_container_width=True)

# Call-out: skills most in need of instruction
low_skills = writing_df[writing_df["Students Showing Skill (%)"] < 60].sort_values(
    "Students Showing Skill (%)"
)
if not low_skills.empty:
    st.warning(
        "**Skills to Prioritize in Mini-Lessons:**\n\n"
        + "\n".join(
            f"- **{row['Skill']}** — only {row['Students Showing Skill (%)']}% of students show this skill"
            for _, row in low_skills.iterrows()
        )
    )
else:
    st.success("All writing skills are above 60%. Continue reinforcing explanation and connection strategies.")

st.divider()

# ── Student Writing Skill Analysis ───────────────────────────────────────────
st.subheader("📋 Student Writing Skill Analysis")
st.caption(
    "Individual student writing skill profiles based on sample SCR practice data. "
    "Proficient = 70% or above. Developing = 50–69%. Needs Support = below 50%."
)

tab_overview, tab_support, tab_groups, tab_profiles = st.tabs([
    "Skill Overview",
    "Students Needing Support",
    "Small Group Suggestions",
    "Individual Profiles",
])

# ── Helpers used across tabs ──────────────────────────────────────────────────
PROFICIENT  = 70
DEVELOPING  = 50
GROUP_THRESHOLD = 60  # below this → flagged for grouping

def skill_level(score):
    if score >= PROFICIENT:
        return "Proficient"
    elif score >= DEVELOPING:
        return "Developing"
    return "Needs Support"

def student_weak_skills(student):
    return [s for s in WRITING_SKILL_LABELS if student[s] < GROUP_THRESHOLD]

def assign_group(student):
    weak = student_weak_skills(student)
    cite_weak    = student["Citing Evidence"]     < GROUP_THRESHOLD
    explain_weak = student["Explaining Evidence"] < GROUP_THRESHOLD
    connect_weak = student["Connecting Back"]     < GROUP_THRESHOLD
    if len(weak) >= 4:
        return "Intensive Support"
    elif cite_weak and explain_weak:
        return "Evidence Writing"
    elif connect_weak:
        return "Connecting Back"
    return "On Track"

# ── Tab 1 — Skill Overview ────────────────────────────────────────────────────
with tab_overview:
    # Heatmap: students × skills
    short_labels = ["Answering", "Citing", "Explaining", "Grammar", "Organization", "Connecting"]
    z_data  = [[s[skill] for skill in WRITING_SKILL_LABELS] for s in STUDENT_WRITING_SKILLS]
    y_names = [s["name"] for s in STUDENT_WRITING_SKILLS]

    fig_heat = go.Figure(data=go.Heatmap(
        z=z_data,
        x=short_labels,
        y=y_names,
        colorscale=[[0.0, "#d73027"], [0.50, "#fee08b"], [0.70, "#91cf60"], [1.0, "#1a9850"]],
        zmin=0, zmax=100,
        text=z_data,
        texttemplate="%{z}%",
        textfont={"size": 10},
    ))
    fig_heat.update_layout(
        title="Writing Skill Scores — All Students",
        height=390,
        margin=dict(l=160, t=50),
        xaxis_title="Writing Skill",
        yaxis_title="Student",
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    st.caption("🟢 Green = Proficient (70%+)   🟡 Yellow = Developing (50–69%)   🔴 Red = Needs Support (<50%)")

    # Per-skill breakdown: select a skill to see who falls where
    st.markdown("---")
    selected_skill = st.selectbox("View students by proficiency level for:", WRITING_SKILL_LABELS)

    proficient_students  = [s["name"] for s in STUDENT_WRITING_SKILLS if s[selected_skill] >= PROFICIENT]
    developing_students  = [s["name"] for s in STUDENT_WRITING_SKILLS if DEVELOPING <= s[selected_skill] < PROFICIENT]
    needs_support_students = [s["name"] for s in STUDENT_WRITING_SKILLS if s[selected_skill] < DEVELOPING]

    col_p, col_d, col_n = st.columns(3)
    with col_p:
        st.success(f"**✅ Proficient ({len(proficient_students)})**")
        for name in proficient_students:
            st.markdown(f"- {name}")
    with col_d:
        st.warning(f"**📈 Developing ({len(developing_students)})**")
        for name in developing_students:
            st.markdown(f"- {name}")
    with col_n:
        st.error(f"**⚠️ Needs Support ({len(needs_support_students)})**")
        for name in needs_support_students:
            st.markdown(f"- {name}")

# ── Tab 2 — Students Needing Support ─────────────────────────────────────────
with tab_support:
    st.markdown(
        "Students listed below have at least one writing skill below 70%. "
        "Priority is based on how many skills are below the developing threshold (50%)."
    )

    support_rows = []
    for s in STUDENT_WRITING_SKILLS:
        below_proficient = [skill for skill in WRITING_SKILL_LABELS if s[skill] < PROFICIENT]
        below_developing = [skill for skill in WRITING_SKILL_LABELS if s[skill] < DEVELOPING]
        if below_proficient:
            support_rows.append({
                "Student":            s["name"],
                "Skills Below 70%":   len(below_proficient),
                "Skills Below 50%":   len(below_developing),
                "Most Critical Needs": ", ".join(below_developing) if below_developing else "—",
            })

    support_rows.sort(key=lambda r: (-r["Skills Below 50%"], -r["Skills Below 70%"]))

    for row in support_rows:
        if row["Skills Below 50%"] >= 4:
            priority_label = "🔴 High Priority"
        elif row["Skills Below 50%"] >= 2:
            priority_label = "🟡 Moderate Priority"
        else:
            priority_label = "🟢 Monitor"

        with st.expander(f"{priority_label} — {row['Student']}"):
            col_a, col_b = st.columns(2)
            col_a.metric("Skills Not Yet Proficient", row["Skills Below 70%"])
            col_b.metric("Skills Needing Reteaching", row["Skills Below 50%"])
            if row["Most Critical Needs"] != "—":
                st.warning(f"**Reteach immediately:** {row['Most Critical Needs']}")
            developing_list = [
                skill for skill in WRITING_SKILL_LABELS
                if DEVELOPING <= next(s[skill] for s in STUDENT_WRITING_SKILLS if s["name"] == row["Student"]) < PROFICIENT
            ]
            if developing_list:
                st.info(f"**Continue developing:** {', '.join(developing_list)}")

    if not support_rows:
        st.success("All students are currently proficient in all writing skills.")

# ── Tab 3 — Small Group Suggestions ──────────────────────────────────────────
with tab_groups:
    st.markdown(
        "Students with shared writing weaknesses are grouped below. "
        "Each group suggests a mini-lesson focus to target their shared skill gap."
    )

    # Assign every student to a group
    group_members = {"Intensive Support": [], "Evidence Writing": [], "Connecting Back": [], "On Track": []}
    for s in STUDENT_WRITING_SKILLS:
        group_members[assign_group(s)].append(s["name"])

    group_info = {
        "Intensive Support": {
            "icon":       "🔴",
            "focus":      "All writing skills — ACE/RACE structure, grammar, and organization",
            "lesson":     "Begin with answering the prompt, then build step-by-step to citing and explaining. Use sentence stems for every part of ACE.",
            "frequency":  "Daily or near-daily small-group sessions recommended.",
        },
        "Evidence Writing": {
            "icon":       "🟡",
            "focus":      "Citing and Explaining Evidence",
            "lesson":     "Practice the C and E steps of ACE. Focus on how to quote the text correctly, and then how to write an explanation sentence using 'This shows that...' or 'This means that...'",
            "frequency":  "2–3 times per week for 15–20 minutes.",
        },
        "Connecting Back": {
            "icon":       "🟡",
            "focus":      "Connecting Evidence Back to the Prompt",
            "lesson":     "Students can cite and explain, but need practice closing their response. Mini-lesson: write a strong final sentence using 'Therefore...' or 'This proves that...' and explain why it matters.",
            "frequency":  "1–2 times per week, brief review.",
        },
        "On Track": {
            "icon":       "🟢",
            "focus":      "Enrichment — deeper analysis and elaboration",
            "lesson":     "These students can begin working on longer, multi-evidence responses and more sophisticated explanation language.",
            "frequency":  "Peer mentoring or independent enrichment tasks.",
        },
    }

    for group_name, info in group_info.items():
        members = group_members[group_name]
        if not members:
            continue
        with st.expander(f"{info['icon']} **{group_name}** — {len(members)} student(s)"):
            st.markdown(f"**Students:** {', '.join(members)}")
            st.markdown(f"**Mini-lesson focus:** {info['focus']}")
            st.info(f"**Suggested activity:** {info['lesson']}")
            st.caption(f"Suggested frequency: {info['frequency']}")

# ── Tab 4 — Individual Profiles ───────────────────────────────────────────────
with tab_profiles:
    student_names = [s["name"] for s in STUDENT_WRITING_SKILLS]
    selected_name = st.selectbox("Choose a student to view:", student_names)
    student = next(s for s in STUDENT_WRITING_SKILLS if s["name"] == selected_name)

    scores = [student[skill] for skill in WRITING_SKILL_LABELS]
    bar_colors = [
        "#1a9850" if sc >= PROFICIENT else "#fee08b" if sc >= DEVELOPING else "#d73027"
        for sc in scores
    ]

    fig_profile = go.Figure(go.Bar(
        x=scores,
        y=WRITING_SKILL_LABELS,
        orientation="h",
        marker_color=bar_colors,
        text=[f"{sc}%" for sc in scores],
        textposition="outside",
    ))
    fig_profile.update_layout(
        title=f"Writing Skill Profile — {selected_name}",
        xaxis=dict(range=[0, 115], title="Score (%)"),
        height=320,
        margin=dict(l=200),
    )
    fig_profile.add_vline(
        x=70, line_dash="dash", line_color="gray",
        annotation_text="Proficient (70%)", annotation_position="top right",
    )
    st.plotly_chart(fig_profile, use_container_width=True)

    # Text summary
    strengths   = [skill for skill in WRITING_SKILL_LABELS if student[skill] >= PROFICIENT]
    developing  = [skill for skill in WRITING_SKILL_LABELS if DEVELOPING <= student[skill] < PROFICIENT]
    reteach     = [skill for skill in WRITING_SKILL_LABELS if student[skill] < DEVELOPING]

    col_s, col_d, col_r = st.columns(3)
    with col_s:
        st.success(f"**✅ Proficient ({len(strengths)})**")
        for skill in strengths:
            st.markdown(f"- {skill}")
    with col_d:
        st.warning(f"**📈 Developing ({len(developing)})**")
        for skill in developing:
            st.markdown(f"- {skill}")
    with col_r:
        st.error(f"**⚠️ Needs Reteaching ({len(reteach)})**")
        for skill in reteach:
            st.markdown(f"- {skill}")

    group = assign_group(student)
    group_icons = {"Intensive Support": "🔴", "Evidence Writing": "🟡", "Connecting Back": "🟡", "On Track": "🟢"}
    st.markdown(f"**Suggested Group:** {group_icons[group]} {group}")
