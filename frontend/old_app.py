import streamlit as st
import requests

FastAPI_url = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Heart Disease Prediction APP",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("HeartGuard AI")
st.subheader("Heart Disease Risk Prediction")
st.write(
    "Enter patient information below to receive a machine-learning based risk prediction."
)

# check backend status
if st.button("Check API Status"):
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

    st.write("DEMOGRAPHICS")

    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Age", 
            min_value=1, 
            max_value=120, 
            value=55)

    with col2:    
        sex = st.selectbox(
            "Sex", 
            [0,1], 
            format_func=lambda x: "Female" if x == 0 else "Male")

    st.divider()
    st.write("Vitals & Labs")

    col1, col2 = st.columns(2)

    with col1:

        resting_bp = st.number_input(
            "Resting Blood Pressure (mmHg)",
            min_value=50,
            max_value=250,
            value=140
        )

        cholesterol = st.number_input(
            "Serum Cholesterol (mg/dL)",
            min_value=100,
            max_value=700,
            value=240
        ) 

        max_heart_rate = st.number_input(
            "Max Heart Rate Achieved",
            min_value=60,
            max_value=220,
            value=150
        )

    with col2:

        oldpeak = st.number_input(
            "St depression (oldpeak)",
            min_value=0.0,
            max_value=10.0,
            value=5.2,
        )

        fasting_bs = st.selectbox(
            "Fasting Blood Sugar ",
            [0,1],
            format_func= lambda x: "No (≤120 mg/dl)" if x == 0 else "Yes (>120 mg/dl)"
        )

        exercise_angina = st.selectbox(
            "Exercise Induced Angina",
            [0,1],
            format_func= lambda x: "No" if x == 0 else "Yes"
        )

    st.divider()
    st.write("CARDIAC TESTS")

    col1, col2 = st.columns(2)

    with col1:

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

        resting_ecg_labels = {
            0: "Normal",
            1: "ST-T Wave Abnormality",
            2: "Left Ventricular Hypertrophy"
        }
        resting_ecg = st.selectbox(
            "Resting ECG",
            list(resting_ecg_labels),
            format_func=resting_ecg_labels.get
        )

        st_slope_labels = {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping"
        }
        st_slope= st.selectbox(
            "St Segement Slope (peak exercise)",
            list(st_slope_labels),
            format_func= st_slope_labels.get

        )

    with col2:

        cardiac_risk_labels = {
            0: "0 – No Major Arteries Blocked",
            1: "1 – One Major Artery Blocked",
            2: "2 – Two Major Arteries Blocked",
            3: "3 – Three Major Arteries Blocked (High Risk)",
            4: "4 – Atypical Reading"
        }
        cardiac_risk = st.selectbox(
            "Major Vessels Colored by Fluoroscopy",
            list(cardiac_risk_labels),
            format_func= cardiac_risk_labels.get
        )

        thallium_stress_test_labels = {
            0: "Normal",
            1: "Fixed Defect",
            2: "Reversable Defect",
            3: "Not specified"
        }
        thallium_stress_test = st.selectbox(
            "Thallium Stress Test Result",
            list(thallium_stress_test_labels),
            format_func=thallium_stress_test_labels.get
        )

        
    submitted = st.form_submit_button("Predict Heart Disease Risk")
        


# if user submits the form

if submitted:

    patient_data = {

        "age": age,
        "sex": sex,
        "chest_pain_type": chest_pain_type,
        "resting_bp": resting_bp,
        "cholesterol": cholesterol,
        "fasting_bs": fasting_bs,
        "resting_ecg": resting_ecg,
        "max_heart_rate": max_heart_rate,
        "exercise_angina": exercise_angina,
        "oldpeak": oldpeak,
        "st_slope": st_slope,
        "cardiac_risk": cardiac_risk,
        "thallium_stress_test": thallium_stress_test

    }

    try:
        response = requests.post(f"{FastAPI_url}/predict", json=patient_data)

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]
            probability = result["probability"]
            risk = result["risk"]
            message = result["message"]

            # Print Result

            st.divider()

            st.subheader("Prediction Result")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Prediction",
                    "Heart Disease"
                    if prediction == 1
                    else "No Heart Disease"
                )

            with col2:

                st.metric(
                    "Probability", 
                    f"{probability * 100:.2f}%")

            with col3:

                st.metric(
                    "Risk Level", 
                    risk
                )

            # Display message
            if risk == "High":

                st.error(
                    "High predicted risk based on the model."
                )

            elif risk == "Moderate":

                st.warning(
                    "Moderate predicted risk based on the model."
                )

            else:

                st.success(
                    "Low predicted risk based on the model."
                )         

        else:
            st.error(f"Error: Status code {response.status_code}")

    except requests.exceptions.ConnectionError:
            st.error("Could not connect to the FastAPI backend. Is it running?")