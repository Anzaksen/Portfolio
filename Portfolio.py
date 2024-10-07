import streamlit as st

st.sidebar.radio("Go to section:", ["My Projects", "My Skills", "My Personality & Work Ethic"])

st.markdown("# Introduction #")
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./profile_image.jpg", width=230)

with col2:
    st.title("Dape Alexander Naanret", anchor=False)
    st.write("Data Analyst,  interested in digging through data and uncovering meaningful insights.")
    st.button("✉️ Contact Me")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown("### My Projects ###")
st.write(
    """
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("My Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas, e.t.c), SQL.
    - Data Visualization: PowerBi, , Plotly.
    - Modeling: Machine Learning, Deep learning
    """
)


# --- About ---
st.write("\n")
st.subheader("My Personality & Work Ethic", anchor=False)
st.write(
    """
   I am a hard worker and always willing to go the extra mile to get the job done. 
   I am a hard worker and a highly motivated and results-oriented individual. 
   I am eager to learn more about your company and the role that I can play in its success.
    I am confident that I can be a valuable asset to your team."""
)
