import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Anzaksen", page_icon=":material/bolt:")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

#st.sidebar.radio("Go to section:", ["Introduction", "My Projects", "My Skills", "My Personality & Work Ethic"])

#st.markdown("# Introduction #")
#st.markdown("---")
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./profile_image.png", use_column_width=True)

with col2:
    st.title("Dape Alexander Naanret", anchor=False)
    st.write("A Data Analyst,  interested in digging through data and uncovering meaningful insights.")
    pdf_file_path = "Alexander_Dape_Resume.pdf"  # Replace 'sample.pdf' with the name of your file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download My Resume",
                           data=pdf_bytes,
                           file_name="My_Resume.pdf",
                           mime="application/pdf")
    
        


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown("# My Projects #")
st.markdown("""
    <hr style="border:2px solid yellow;">
    """, unsafe_allow_html=True)
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
st.markdown("""
    <hr style="border:2px solid yellow;">
    """, unsafe_allow_html=True)
cl1, cl2 = st.columns(2, gap="small", vertical_alignment="center")
with cl1:
    st.write(
        """
        - Programming: Python (Scikit-learn, Pandas, e.t.c), SQL.
        - Data Visualization: PowerBi, Seaborn, Plotly.
        - Modeling: Machine Learning, Deep learning
        """
    )
with cl2:
    path = "./skill.json"
    with open(path,"r") as file: 
        url = json.load(file) 
    
    st_lottie(url, 
        reverse=True, 
        height=250, 
        width=250, 
        speed=1, 
        loop=True, 
        quality='high'
    )


# --- About ---
st.write("\n")
st.markdown("# My Personality & Work Ethic #")
st.markdown("""
    <hr style="border:2px solid yellow;">
    """, unsafe_allow_html=True)
l1, l2 = st.columns(2, gap="small", vertical_alignment="center")
with l1:
    path = "./Ani.json"
    with open(path,"r") as file: 
        url = json.load(file) 
    
    st_lottie(url, 
        reverse=True, 
        height=300, 
        width=250, 
        speed=1, 
        loop=True, 
        quality='high'
    )
with l2:
    st.write(
        """ 
       I am a hard worker and a highly motivated and results-oriented individual. 
       I am eager to learn more about your company and the role that I can play in its success.
        I am confident that I can be a valuable asset to your team."""
    )


st.write("\n")
st.markdown("# Contact Me #")
st.markdown("""
    <hr style="border:2px solid yellow;">
    """, unsafe_allow_html=True)
co1, co2, co3, co4 = st.columns(4, gap="small", vertical_alignment="center")
with co1:
    st.markdown('''
    <p style="color:#ffe34b; font-size:28px; font-weight:bold;">
        <a href="https://www.linkedin.com/in/alexanderdape" target="_blank" style="color:#ffe34b; text-decoration:none;">
            LinkedIn
        </a>
    </p>
    ''', unsafe_allow_html=True)
with co2:
    st.markdown('''
    <p style="color:#ffe34b; font-size:28px; font-weight:bold;">
        <a href="https://github.com/anzaksen" target="_blank" style="color:#ffe34b; text-decoration:none;">
            Github
        </a>
    </p>
    ''', unsafe_allow_html=True)
with co3:
    st.markdown('''
    <p style="color:#ffe34b; font-size:28px; font-weight:bold;">
        <a href="https://twitter.com/DAPE_AN" target="_blank" style="color:#ffe34b; text-decoration:none;">
            Twitter
        </a>
    </p>
    ''', unsafe_allow_html=True)
with co4:
    st.markdown('''
    <p style="color:#ffe34b; font-size:28px; font-weight:bold;">
        <a href="mailto:dapealexander@gmail.com" target="_blank" style="color:#ffe34b; text-decoration:none;">
            Gmail
        </a>
    </p>
    ''', unsafe_allow_html=True)
