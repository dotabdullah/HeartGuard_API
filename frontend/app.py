import streamlit as st
import requests

FastAPI_url = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Heart Disease Prediction APP",
)

st.title("HeartGuard AI")
st.subheader("Heart Disease Risk Prediction")
st.write(
    "Enter patient information below to receive a machine-learning based risk prediction."
)

# check backend status
if st.button("check status"):
    try:
        reponse = requests.get(f"{FastAPI_url}/health")
        if reponse.status_code == 200:
            st.success(reponse.json().get("status"))
        else:
            st.error("Backend return an error. Please check the backend server.")   

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI backend. Is it running?")         


# Patient Form
with st.form("patient_form"):

    st.subheader("Patient Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age", 
            min_value=1, 
            max_value=120, 
            value=55)
        
        sex = st.selectbox(
            "Sex", 
            [0,1], 
            format_func=lambda x: "Female" if x == 0 else "Male")
        
        chest_pain_labels = {
            0: "Typical Angina",
            1: "Atypical Angina",
            2: "Non-anginal Pain",
            3: "Asymptomatic",
        }
        
        chest_pain_type = st.selectbox(
            "Chest Pain Type",
            list(chest_pain_labels),
            format_func=chest_pain_labels.get,
        )
