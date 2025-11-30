import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Graphs")
df = pd.read_csv("Student_performance_data _.csv")
df_sample = df.head(100)  # limit to first 100 rows

# --- Setup session state for buttons ---
if "show_scatter" not in st.session_state:
    st.session_state.show_scatter = False
if "show_bar" not in st.session_state:
    st.session_state.show_bar = False
if "show_pie" not in st.session_state:
    st.session_state.show_pie = False

# --- Toggle buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Scatter Chart"):
        st.session_state.show_scatter = not st.session_state.show_scatter
with col2:
    if st.button("Bar Chart"):
        st.session_state.show_bar = not st.session_state.show_bar
with col3:
    if st.button("Pie Chart"):
        st.session_state.show_pie = not st.session_state.show_pie

# --- Scatter Chart ---
if st.session_state.show_scatter:
    st.subheader("GPA vs Weekly Study Time")
    fig = px.scatter(
        df_sample,
        x='StudyTimeWeekly',
        y='GPA',
        size='GPA',
        color='GPA',
        hover_data=['StudyTimeWeekly', 'GPA'],
        title='GPA to Weekly Study Time'
    )
    fig.update_traces(marker=dict(size=18, line=dict(width=3, color='DarkSlateGrey')))
    fig.update_yaxes(range=[df_sample['GPA'].min() - 0.2, df_sample['GPA'].max() + 0.2])
    fig.update_layout(
        height=800,
        width=1000,
        title_font_size=36,
        xaxis_title_font_size=24,
        yaxis_title_font_size=24,
        legend_font_size=20
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Bar Chart ---
if st.session_state.show_bar:
    st.subheader('Bar Chart: GPA vs Weekly Study Time')
    st.bar_chart(df_sample[['GPA','StudyTimeWeekly']], use_container_width=True)

# --- Pie Chart ---
if st.session_state.show_pie:
    st.subheader('Students with GPA > 3.5: Weekly Study Time')
    df_high = df[df['GPA'] > 3.5]
    bins = [0, 5, 10, 15, 20, 25]
    labels = ['0-5', '6-10', '11-15', '16-20', '21-25']
    df_high['StudyBin'] = pd.cut(df_high['StudyTimeWeekly'], bins=bins, labels=labels, right=True)
    study_counts = df_high['StudyBin'].value_counts().sort_index().reset_index()
    study_counts.columns = ['StudyBin', 'Count']

    fig_pie = px.pie(
        study_counts,
        names='StudyBin',
        values='Count',
        hole=0,
        title='Students with GPA > 3.5: Weekly Study Time',
        height=700,
        width=700
    )
    fig_pie.update_traces(textinfo='label+percent', textfont_size=20, pull=[0]*len(study_counts))
    fig_pie.update_layout(title_font_size=25, legend_font_size=18)
    st.plotly_chart(fig_pie, use_container_width=True)

# --- UI Styling for Buttons ---
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    box-shadow: 3px 3px 10px grey;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)
