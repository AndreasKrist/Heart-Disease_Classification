import streamlit as st
import joblib
import numpy as np


# Load the trained model
model = joblib.load('heart-disease-model.joblib')

# Streamlit Web App
st.title("Heart Disease Prediction App")

# Display the heart image
st.image("image.jpg", caption="The Human Heart", use_container_width=True)
st.text("Heart disease refers to a range of conditions affecting the heart's structure and function, including coronary artery disease, heart attacks, and congenital heart defects. Symptoms may include chest pain, shortness of breath, and fatigue. Regular check-ups, a healthy lifestyle, and early detection are key to managing heart health.")


# User inputs
st.header("Enter Your Information")
name = st.text_input("Name", placeholder="Your Name ...")

age = st.number_input("Age", value=30)

sex = st.selectbox("Sex", ["Male", "Female"])  # Male (1), Female (0)

cp = st.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina (0)",
        "Atypical Angina (1)",
        "Non-anginal Pain (2)",
        "Asymptomatic (3)"
    ]
)

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", value=120)

chol = st.number_input("Cholesterol (mg/dL)", value=200)

fbs = st.selectbox(
    "Fasting Blood Sugar (> 120 mg/dL)",
    ["True (1)", "False (0)"]
)

restecg = st.selectbox(
    "Resting ECG Results",
    [
        "Nothing to Note (0)",
        "ST-T Wave Abnormality (1)",
        "Possible Left Ventricular Hypertrophy (2)"
    ]
)

thalach = st.number_input("Maximum Heart Rate Achieved", value=150)

exang = st.selectbox(
    "Exercise Induced Angina",
    ["Yes (1)", "No (0)"]
)

oldpeak = st.number_input("ST Depression Induced by Exercise", value=0.0)

slope = st.selectbox(
    "Slope of Peak Exercise ST Segment",
    ["Upsloping (0)", "Flat Sloping (1)", "Downsloping (2)"]
)

ca = st.slider("Number of Major Vessels (0 to 4)", 0, 4)

thal = st.selectbox(
    "Thalassemia",
    ["Normal (0)", "Fixed Defect (1)", "Reversible Defect (2)"]
)

# Map inputs to numerical values
sex = 1 if sex == "Male" else 0
cp = int(cp.split("(")[1][0])
fbs = int(fbs.split("(")[1][0])
restecg = int(restecg.split("(")[1][0])
exang = int(exang.split("(")[1][0])
slope = int(slope.split("(")[1][0])
thal = int(thal.split("(")[1][0])

# Create input array for the model
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

# Predict button
if st.button("Predict"):
    result = model.predict(input_data)[0]  # Predict using the loaded model
    if result == 1:
        st.error(f"{name}, you may have heart disease. Please consult a doctor.")
    else:
        st.success(f"{name}, you are unlikely to have heart disease. Keep staying healthy!")
