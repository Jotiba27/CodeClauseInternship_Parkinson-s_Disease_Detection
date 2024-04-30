# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:01:37 2024

@author: dudhb
"""
import os
import pickle
import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Parkinson's Disease Prediction",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Load the saved model
parkinsons_model = pickle.load(open('D:/CodeClause/multiple-disease-prediction-streamlit-app-main/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
            color: #333;
        }
        .sidebar .sidebar-content .block-container {
            padding: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🧬 Parkinson's Disease Prediction")
st.sidebar.write("Please provide the required information for prediction.")

# Main content
st.title("🧠 Parkinson's Disease Prediction using Machine Learning")
image = Image.open("D:\CodeClause\multiple-disease-prediction-streamlit-app-main\Images\parkinson.jpg")
st.image(image, caption='Parkinsons Disease Prediction', use_column_width=True)

# Create input fields for user data
st.subheader("Input Data")

# Using Streamlit's columns to make the input fields responsive
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    fo = st.number_input('MDVP:Fo(Hz)', min_value=0.0, step=0.1)
    fhi = st.number_input('MDVP:Fhi(Hz)', min_value=0.0, step=0.1)
    flo = st.number_input('MDVP:Flo(Hz)', min_value=0.0, step=0.1)
    Jitter_percent = st.number_input('MDVP:Jitter(%)', min_value=0.0, step=0.1)
    Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', min_value=0.0, step=0.1)
    RAP = st.number_input('MDVP:RAP', min_value=0.0, step=0.1)
    PPQ = st.number_input('MDVP:PPQ', min_value=0.0, step=0.1)

with col3:
    DDP = st.number_input('Jitter:DDP', min_value=0.0, step=0.1)
    Shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, step=0.1)
    Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', min_value=0.0, step=0.1)
    APQ3 = st.number_input('Shimmer:APQ3', min_value=0.0, step=0.1)
    APQ5 = st.number_input('Shimmer:APQ5', min_value=0.0, step=0.1)
    APQ = st.number_input('MDVP:APQ', min_value=0.0, step=0.1)
    DDA = st.number_input('Shimmer:DDA', min_value=0.0, step=0.1)

NHR = st.number_input('NHR', min_value=0.0, step=0.1)
HNR = st.number_input('HNR', min_value=0.0, step=0.1)
RPDE = st.number_input('RPDE', min_value=0.0, step=0.1)
DFA = st.number_input('DFA', min_value=0.0, step=0.1)
spread1 = st.number_input('spread1', min_value=0.0, step=0.1)
spread2 = st.number_input('spread2', min_value=0.0, step=0.1)
D2 = st.number_input('D2', min_value=0.0, step=0.1)
PPE = st.number_input('PPE', min_value=0.0, step=0.1)

# Predict Parkinson's Disease
if st.button("Predict Parkinson's Disease"):
    user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,
                  DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR,
                  HNR, RPDE, DFA, spread1, spread2, D2, PPE]

    user_input = [float(x) for x in user_input]

    parkinsons_prediction = parkinsons_model.predict([user_input])

    if parkinsons_prediction[0] == 1:
        st.success("The person has Parkinson's disease")
    else:
        st.success("The person does not have Parkinson's disease")
