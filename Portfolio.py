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
col1, col2 = st.columns([1.5,1], gap="small", vertical_alignment="center")
with col1:
    st.image("Photoroom-20250213_103621.png", use_container_width=True)

with col2:
    st.title("Engr. Dape Alexander Naanret", anchor=False)
    st.write("A Data Analyst,  interested in digging through data and uncovering meaningful insights.")
    pdf_file_path = "Alexander_Dape_Resume.pdf"  # Replace 'sample.pdf' with the name of your file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download My Resume",
                           data=pdf_bytes,
                           file_name="Alexander Dape Resume.pdf",
                           mime="application/pdf")
    
        


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown("# My Projects #")
st.markdown("""
    <hr style="border:2px #6d8d8c;">
    """, unsafe_allow_html=True)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="https://huggingface.co/spaces/Anzaksen/Hiv-response" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            IISDAS:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    IISDAS is a Student Data Analytics system with 3 distinct features:
    - A Dashboard visualizing distributions within student results to identify patterns.
    - A result predictor which is a CATBOOST model trained to predict students' results based on external factors.
    - A Large Language Model (LLM) finetuned with the results to help educators get answers to questions in a chat-based, user-friendly manner.
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="https://huggingface.co/spaces/Anzaksen/Hiv-response" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            HIV Treatment Response Prediction:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    - Trained several regression models to predict a patient's CD4 and Viral count  after a session of treatment.
    - Evaluated the models and selected the best 3 to be deployed on huggingface
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="https://huggingface.co/spaces/Anzaksen/breast_cancer_malignancy_detector" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Breast Cancer Malignancy Detector:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    - Trained a Random Forest Classifier to detect if a cancer is malign or benignant using several parameters.
    - Deloyed the model on Huggingface.
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="https://github.com/Anzaksen/world_population" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            World Population:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    A dashboard showing the world population trend from 1970 to 2022.
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="https://github.com/Anzaksen/Suicide_rates_1985_to_2016" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Suicide Rates:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    Time series analysis of reported suicide cases from 1985 to 2016.
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="https://github.com/Anzaksen/Ky_louisville_Police_Driver_Data_Analysis" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Kentucky Open Policing:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    EDA on open polocing data on police stops in kentucky, louisville from 2015 to 2018.
    """
)

# --- SKILLS ---
st.write("\n")
st.markdown("# My Skills #")
st.markdown("""
    <hr style="border:2px #6d8d8c;">
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
    <hr style="border:2px #6d8d8c;">
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
    <hr style="border:2px #6d8d8c;">
    """, unsafe_allow_html=True)
co1, co2, co3, co4 = st.columns(4, gap="small", vertical_alignment="center")
with co1:
    st.markdown('''
    <p style="color:#6d8d8c; font-size:28px; font-weight:bold;">
        <a href="https://www.linkedin.com/in/alexanderdape" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            LinkedIn
        </a>
    </p>
    ''', unsafe_allow_html=True)
with co2:
    st.markdown('''
    <p style="color:#6d8d8c; font-size:28px; font-weight:bold;">
        <a href="https://github.com/anzaksen" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Github
        </a>
    </p>
    ''', unsafe_allow_html=True)
with co3:
    st.markdown('''
    <p style="color:#6d8d8c; font-size:28px; font-weight:bold;">
        <a href="https://twitter.com/DAPE_AN" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Twitter
        </a>
    </p>
    ''', unsafe_allow_html=True)
with co4:
    st.markdown('''
    <p style="color:#6d8d8c; font-size:28px; font-weight:bold;">
        <a href="mailto:dapealexander@gmail.com" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Gmail
        </a>
    </p>
    ''', unsafe_allow_html=True)
