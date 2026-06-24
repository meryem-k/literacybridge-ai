import sys
import os
import streamlit as st
import pandas as pd
import plotly.express as px

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.teacher_data import STUDENTS, WEEKLY_PROGRESS

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
