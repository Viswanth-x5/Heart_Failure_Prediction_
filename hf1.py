import streamlit as st
import pandas as pd
import numpy as np
import pickle

with open('rf_model_heart_failure.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Heart Failure Prediction Application")

st.sidebar.header("Patient Data")

def user_input_features():
    anaemia = st.sidebar.selectbox('Anaemia', [0, 1])
    diabetes = st.sidebar.selectbox('Diabetes', [0, 1])
    high_blood_pressure = st.sidebar.selectbox('High Blood Pressure', [0, 1])
    sex = st.sidebar.selectbox('Sex', [0, 1])
    smoking = st.sidebar.selectbox('Smoking', [0, 1])
    age = st.sidebar.number_input('Age', min_value=0)
    creatinine_phosphokinase = st.sidebar.number_input('Creatinine Phosphokinase', min_value=0)
    ejection_fraction = st.sidebar.number_input('Ejection Fraction', min_value=0)
    platelets = st.sidebar.number_input('Platelets', min_value=0.0)
    serum_creatinine = st.sidebar.number_input('Serum Creatinine', min_value=0.0)
    serum_sodium = st.sidebar.number_input('Serum Sodium', min_value=0)
    time = st.sidebar.number_input('Time', min_value=0)
    
    data = {'anaemia': anaemia,
            'diabetes': diabetes,
            'high_blood_pressure': high_blood_pressure,
            'sex': sex,
            'smoking': smoking,
            'age': age,
            'creatinine_phosphokinase': creatinine_phosphokinase,
            'ejection_fraction': ejection_fraction,
            'platelets': platelets,
            'serum_creatinine': serum_creatinine,
            'serum_sodium': serum_sodium,
            'time': time}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("Patient Data")
st.write(df)

if st.button('Predict'):
    prediction = model.predict(df)
    prediction_proba = model.predict_proba(df)

    st.subheader("Prediction")
    heart_failure_risk = np.array(['No', 'Yes'])
    st.write(f"Heart Failure: {heart_failure_risk[prediction][0]}")

    st.subheader("Prediction Probability")
    st.write(prediction_proba)
