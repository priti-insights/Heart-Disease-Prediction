import pandas as pd
import numpy as np
import pickle
import streamlit as st

# Load the trained model
load_model = pickle.load(open("heart_model.pkl","rb"))

# 🎨 Page config
st.set_page_config(
    page_title="💖 Heart Health Prediction",
    layout="centered"
)

# 🎨 Custom CSS
st.markdown(
    """
    <style>
    /* Gradient background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
        background-attachment: fixed;
    }

    /* Glassmorphism card */
    .main-content {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(8px);
        padding: 2rem;
        border-radius: 1rem;
        max-width: 800px;
        margin: 2rem auto;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    /* Title animations */
    h1 {
        color: #B22222;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    h2, h3 {
        color: #333;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Input label colors */
    label {
        font-weight: bold;
        color: #444 !important;
    }

    /* Submit button */
    div.stButton > button {
        background-color: #ff6f61;
        color: white;
        padding: 0.5rem 2rem;
        border-radius: 8px;
        border: none;
        font-size: 1rem;
        transition: background 0.3s;
    }
    div.stButton > button:hover {
        background-color: #ff3f2e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Wrap content in a glass card
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

# 🎨 Title
st.title("💖 Heart Health Prediction")

st.markdown(
    "#### Fill in your details to check your heart health status\n---"
)

# Input form
with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120)
        sex = st.selectbox(
            "Gender",
            options=[0, 1],
            help="1 = Male, 0 = Female"
        )
        cp = st.selectbox(
            "Chest Pain Type",
            options=[0, 1, 2, 3]
        )
        trestbps = st.number_input(
            "Resting Blood Pressure (mm Hg)"
        )
        chol = st.number_input(
            "Cholesterol (mg/dL)"
        )
        fbs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dL",
            options=[0,1]
        )
    with col2:
        restecg = st.selectbox(
            "Resting ECG",
            options=[0, 1, 2]
        )
        thalach = st.number_input(
            "Max Heart Rate Achieved"
        )
        exang = st.selectbox(
            "Exercise-Induced Angina",
            options=[0,1]
        )
        oldpeak = st.number_input(
            "Oldpeak (ST depression)"
        )
        slope = st.selectbox(
            "Slope of Peak Exercise ST",
            options=[0,1,2]
        )
        ca = st.selectbox(
            "Number of Major Vessels",
            options=[0,1,2,3,4]
        )
        thal = st.selectbox(
            "Thalassemia",
            options=[0,1,2,3]
        )

    submit_button = st.form_submit_button("🔍 Predict")

# Prediction output
if submit_button:
    output = load_model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    )
    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if output[0] == 0:
        st.success("✅ Prediction: No Heart Disease detected!")
    else:
        st.error("⚠️ Prediction: Heart Disease risk detected!")

# Close main-content div
st.markdown("</div>", unsafe_allow_html=True)

