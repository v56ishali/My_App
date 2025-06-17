import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model_pickle.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("💼 Salary Prediction App")

# Input fields
age = st.number_input("Age", min_value=18, max_value=65, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
job_title = st.selectbox("Job Title", ["Software Engineer", "Data Analyst", "Senior Manager", "Sales Associate", "Director"])
experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=5.0)

# Convert inputs to numeric (same as in training)
gender_map = {"Male": 0, "Female": 1}
education_map = {"Bachelor's": 0, "Master's": 1, "PhD": 2}
job_map = {"Software Engineer": 0, "Data Analyst": 1, "Senior Manager": 2, "Sales Associate": 3, "Director": 4}

input_data = np.array([[age, gender_map[gender], education_map[education], job_map[job_title], experience]])

# Predict
if st.button("Predict Salary"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Salary: ₹{prediction[0]:,.2f}")
