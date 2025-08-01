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
    st.title("Dape Alexander Naanret", anchor=False)
    st.write("A Data Analyst,  interested in digging through data and uncovering meaningful insights.")
    pdf_file_path = "Alexander_Dape_Resume.pdf"  # Replace 'sample.pdf' with the name of your file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()
        st.download_button(label="Download My Resume",
                           data=pdf_bytes,
                           file_name="Alexander_Dape_CV.pdf",
                           mime="application/pdf")
    
        


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.markdown("# My Projects #")
st.markdown("""
    <hr style="border:3px solid #6d8d8c;">
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
        <a href="" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Supplier Relationship Management and Supply Chain Efficiency in Abuja:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    - Analyzed the impact of trust-based relationships, information sharing, and supplier collaboration on the supply chain efficiency of manufacturing firms in Abuja.
    - Used descriptive statistics and logistic regression to quantify the relationship between supplier practices and key performance metrics like cost, lead time, quality, and flexibility.
    - Identified information sharing as the most significant driver of supply chain efficiency, outperforming trust and collaboration in predictive strength.
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            Forecasting Electricity Prices in Germany Using Machine Learning:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    - Conducted time-series analysis on historical electricity price data from the German market to build predictive models.
    - Implemented and evaluated four machine learning models: Linear Regression, Decision Tree, Random Forest, and XGBoost.
    - Assessed and compared model performance using metrics such as RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error).
    - Identified the most accurate model for price forecasting to support decision-making in energy trading and consumption planning.
    - Provided insights on data-driven energy pricing strategies and model suitability for dynamic electricity markets.
    """
)

st.markdown('''
    <p style="color:#6d8d8c; font-size:15px; font-weight:bold;">
        <a href="" target="_blank" style="color:#6d8d8c; text-decoration:none;">
            CNN Architectures for Plant Disease Classification: A Comparative Study:
        </a>
    </p>
    ''', unsafe_allow_html=True)
st.write(
    """
    - Evaluated five CNN architectures (VGG16, DenseNet121, MobileNetV3, EfficientNetB0, NASNetMobile) on the PlantVillage dataset for multi-class plant disease recognition.
    - Trained models using both fine-tuning and feature extraction strategies at different input resolutions (128×128 and 160×160).
    - Applied post-training quantization using TensorFlow Lite to reduce model size and optimize for deployment on mobile and embedded systems.
    - Benchmarked models on three metrics: validation accuracy, inference time (ms), and model size (MB).
    - Identified DenseNet121 as the most balanced model post-quantization, achieving high accuracy with reduced storage requirements.
    - Highlighted critical trade-offs between model performance and resource constraints, offering recommendations for real-world agricultural AI deployment.
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
    <hr style="border:3px solid #6d8d8c;">
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
    <hr style="border:3px solid #6d8d8c;">
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
    <hr style="border:3px solid #6d8d8c;">
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
        <a href="https://twitter.com/anzaksen" target="_blank" style="color:#6d8d8c; text-decoration:none;">
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
