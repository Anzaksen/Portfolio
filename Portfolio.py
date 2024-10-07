import streamlit as st

#st.sidebar.radio("Go to section:", ["Introduction", "My Projects", "My Skills", "My Personality & Work Ethic"])

st.markdown("# Introduction #")
st.markdown("---")
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./profile_image.jpg")

with col2:
    st.title("Dape Alexander Naanret", anchor=False)
    st.write("Data Analyst,  interested in digging through data and uncovering meaningful insights.")
    pdf_file_path = "Alexander_Dape_Resume.pdf"  # Replace 'sample.pdf' with the name of your file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download My Resume",
                           data=pdf_bytes,
                           file_name="My_Resume.pdf",
                           mime="application/pdf")
    
        


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown("---")
st.markdown("# My Projects #")
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
st.markdown("# My Skills #")
st.markdown("---")
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas, e.t.c), SQL.
    - Data Visualization: PowerBi, , Plotly.
    - Modeling: Machine Learning, Deep learning
    """
)


# --- About ---
st.write("\n")
st.markdown("# My Personality & Work Ethic #")
st.markdown("---")
st.write(
    """
   I am a hard worker and always willing to go the extra mile to get the job done. 
   I am a hard worker and a highly motivated and results-oriented individual. 
   I am eager to learn more about your company and the role that I can play in its success.
    I am confident that I can be a valuable asset to your team."""
)
