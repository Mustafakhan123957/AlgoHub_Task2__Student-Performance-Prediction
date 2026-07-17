import streamlit as st
import joblib
import numpy as np
import os

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("About")

st.sidebar.info("""
### Student Performance Prediction System

**Models Used**
- Logistic Regression
- Random Forest

**Developed Using**
- Python
- Scikit-learn
- Streamlit
""")

# -------------------------------
# Load Model
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "student_performance_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("❌ Model file 'student_performance_model.pkl' not found.")
    st.stop()

# -------------------------------
# Main App
# -------------------------------
st.title("🎓 Student Performance Prediction")

st.write("Enter the student's academic information below.")

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=15.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=5
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0,
    max_value=100,
    value=70
)

participation = st.number_input(
    "Participation Score",
    min_value=1,
    max_value=10,
    value=5
)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):

    features = np.array([[
        study_hours,
        attendance,
        assignments,
        previous_marks,
        participation
    ]])

    prediction = model.predict(features)

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(features)

        if prediction[0] == 1:
            st.success("🎉 Prediction: PASS")
            st.write(f"Confidence: {probability[0][1] * 100:.2f}%")
        else:
            st.error("❌ Prediction: FAIL")
            st.write(f"Confidence: {probability[0][0] * 100:.2f}%")
    else:
        if prediction[0] == 1:
            st.success("🎉 Prediction: PASS")
        else:
            st.error("❌ Prediction: FAIL")
