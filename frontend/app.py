import streamlit as st
import requests


# ============================================================
# CONFIGURATION
# ============================================================

FASTAPI_URL = "https://heartguard-api.fastapicloud.dev/"

st.set_page_config(
    page_title="HeartGuard AI",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- Global ---------- */

    .stApp {
        background-color: #0e1117;
        color: #fff
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* ---------- Header ---------- */

    .main-header {
        margin-top: 40px;
        background: rgb(38, 39, 48);
        padding: 30px 35px;
        border-radius: 18px;
        margin-bottom: 25px;
        border: 1px solid #e5e7eb;
    }

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
        color: #fff;
    }

    .main-subtitle {
        font-size: 17px;
        color: #ccc;
        margin-bottom: 0;
    }


    /* ---------- Section Headers ---------- */

    .section-header {
        font-size: 22px;
        font-weight: 700;
        color: #fff;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .section-description {
        color: #acacac;
        font-size: 14px;
        margin-bottom: 18px;
    }


    /* ---------- Cards ---------- */

    .info-card {
        background: white;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        margin-bottom: 20px;
    }


    /* ---------- API Status ---------- */

    .api-status {
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #065f46;
        padding: 10px 16px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 600;
        display: inline-block;
    }


    /* ---------- Result Area ---------- */

    .result-card {
        background: rgb(38, 39, 48);
        padding: 30px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        margin-top: 25px;
        margin-bottom: 30px;
    }

    .result-title {
        font-size: 24px;
        font-weight: 700;
        color: #fff;
        margin-bottom: 20px;
    }

    .result-description {
        color: #ccc;
        font-size: 14px;
    }


    /* ---------- Disclaimer ---------- */

    .disclaimer {
        background: rgb(38, 39, 48);
        border: 1px solid #9f1515;
        padding: 16px 20px;
        border-radius: 12px;
        color: #fff;
        font-size: 13px;
        margin-top: 30px;
    }


    /* ---------- Buttons ---------- */

    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 10px;
        font-weight: 600;
        min-height: 45px;
    }


    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        border-right: 1px solid #e5e7eb;
    }
    

    button[aria-label="Decrement"],
    button[aria-label="Increment"],
    button[aria-haspopup="listbox"],
    button[kind="secondaryFormSubmit"] {
        background-color: #5c0101 !important;
        color: white !important;
        border-color: #a30202 !important;
    }
    button[aria-label="Decrement"]:hover,
    button[aria-label="Increment"]:hover,
    button[aria-haspopup="listbox"]:hover,
    button[kind="secondaryFormSubmit"]:hover {
        background-color: #7d0101 !important;
        border-color: #7d0101 !important;
    }

    @media (max-width: 767px) {
        .main-header {
            margin-top: 20px;
            padding: 25px;
            border-radius: 10px;
        }
        .main-header {
           font-size: 32px;
        }
        .main-subtitle {
            font-size: 16px;
        }
        .disclaimer{
            border-radius: 10px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## ❤️ HeartGuard AI")

    st.caption("Heart Disease Risk Assessment")

    st.divider()

    st.markdown("### About")

    st.write(
        """
        HeartGuard AI provides an estimated heart disease risk assessment based on the patient information provided.
        The assessment is designed to help users understand how multiple health indicators can be evaluated together.
        """
    )

    st.divider()

    st.markdown("### How it works")
    st.write("""
        1. Enter the patient's information.
        2. Review the provided values.
        3. Select Assess Heart Disease Risk.
        4. Review the estimated risk and prediction.
    """)

    st.divider()
    st.markdown("### Backend")

    if st.button("Check API Status", use_container_width=True):

        try:

            response = requests.get(
                f"{FASTAPI_URL}/health",
                timeout=5
            )

            if response.status_code == 200:

                api_data = response.json()

                st.success(
                    f"API Online — {api_data.get('model', 'Model available')}"
                )

            else:

                st.error(
                    "Backend returned an error."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to FastAPI."
            )

        except requests.exceptions.RequestException:

            st.error(
                "Unable to reach the backend."
            )

    st.divider()

    st.caption(
        "HeartGuard AI • Educational ML Prototype"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
<div class="main-header">
    <div class="main-title">
        🩺 HeartGuard AI
    </div>
    <div class="main-subtitle">
        Heart Disease Risk Assessment using Machine Learning
    </div>
</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# API QUICK STATUS
# ============================================================

st.markdown(
        """
        <div class="section-description">
            Enter patient information below to receive a
            model-based heart disease risk estimate.
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# PATIENT FORM
# ============================================================

with st.form("patient_form"):

    # --------------------------------------------------------
    # PATIENT INFORMATION
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-header"> Patient Information</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
            Basic demographic information about the patient.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=55,
            step=1
        )

    with col2:

        sex = st.selectbox(
            "Sex",
            [0, 1],
            format_func=lambda x:
                "Female" if x == 0 else "Male"
        )

    with col3:

        fasting_bs = st.selectbox(
            "Fasting Blood Sugar",
            [0, 1],
            format_func=lambda x:
                "No (≤120 mg/dL)"
                if x == 0
                else "Yes (>120 mg/dL)"
        )


    st.divider()


    # --------------------------------------------------------
    # VITALS & LABS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-header">Vitals & Laboratory Results</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
            Enter the patient's cardiovascular measurements
            and laboratory values.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        resting_bp = st.number_input(
            "Resting Blood Pressure (mmHg)",
            min_value=50,
            max_value=250,
            value=140,
            step=1
        )

    with col2:

        cholesterol = st.number_input(
            "Serum Cholesterol (mg/dL)",
            min_value=100,
            max_value=700,
            value=240,
            step=1
        )

    with col3:

        max_heart_rate = st.number_input(
            "Maximum Heart Rate",
            min_value=60,
            max_value=220,
            value=150,
            step=1
        )


    st.divider()


    # --------------------------------------------------------
    # EXERCISE & ECG
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-header">Exercise & Cardiac Measurements</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
            Exercise-related measurements and cardiac response.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        oldpeak = st.number_input(
            "ST Depression (Oldpeak)",
            min_value=0.0,
            max_value=10.0,
            value=1.0,
            step=0.1
        )

    with col2:

        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            [0, 1],
            format_func=lambda x:
                "No" if x == 0 else "Yes"
        )

    with col3:

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


    st.divider()


    # --------------------------------------------------------
    # CARDIAC TESTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="section-header">Cardiac Tests</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-description">
            Additional cardiac test results used by the
            machine-learning model.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    with col1:

        chest_pain_labels = {
            0: "Typical Angina",
            1: "Atypical Angina",
            2: "Non-anginal Pain",
            3: "Asymptomatic"
        }

        chest_pain_type = st.selectbox(
            "Chest Pain Type",
            list(chest_pain_labels),
            format_func=chest_pain_labels.get
        )


        st_slope_labels = {
            0: "Upsloping",
            1: "Flat",
            2: "Downsloping"
        }

        st_slope = st.selectbox(
            "ST Segment Slope",
            list(st_slope_labels),
            format_func=st_slope_labels.get
        )


    with col2:

        cardiac_risk_labels = {
            0: "0 – No Major Vessels",
            1: "1 – One Major Vessel",
            2: "2 – Two Major Vessels",
            3: "3 – Three Major Vessels",
            4: "4 – Atypical Reading"
        }

        cardiac_risk = st.selectbox(
            "Major Vessels",
            list(cardiac_risk_labels),
            format_func=cardiac_risk_labels.get
        )


        thallium_stress_test_labels = {
            0: "Normal",
            1: "Fixed Defect",
            2: "Reversible Defect",
            3: "Not Specified"
        }

        thallium_stress_test = st.selectbox(
            "Thallium Stress Test",
            list(thallium_stress_test_labels),
            format_func=thallium_stress_test_labels.get
        )


    st.divider()


    # --------------------------------------------------------
    # SUBMIT
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="text-align:center; margin-top:15px;">
            <p style="color:#6b7280;">
                Review the information above before running
                the model assessment.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    submitted = st.form_submit_button(
        "🔍 Assess Heart Disease Risk",
        use_container_width=True
    )


# ============================================================
# PREDICTION
# ============================================================

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


    with st.spinner("Analyzing patient information..."):

        try:

            response = requests.post(
                f"{FASTAPI_URL}/predict",
                json=patient_data,
                timeout=15
            )


            # ------------------------------------------------
            # SUCCESS
            # ------------------------------------------------

            if response.status_code == 200:

                result = response.json()

                prediction = result["prediction"]
                probability = result["probability"]
                risk = result["risk"]

                st.markdown(
                    """
                    <div class="result-card">
                        <div class="result-title">
                            📊 Assessment Result
                        </div>
                        <div class="result-description">
                            The following result represents the
                            machine-learning model's estimate based
                            on the information provided.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


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
                        f"{probability * 100:.2f}%"
                    )


                with col3:

                    st.metric(
                        "Risk Level",
                        risk
                    )


                # --------------------------------------------
                # PROBABILITY
                # --------------------------------------------

                st.markdown("### Model Risk Estimate")

                st.progress(
                    float(probability)
                )

                st.caption(
                    f"Estimated probability: "
                    f"{probability * 100:.2f}%"
                )


                # --------------------------------------------
                # RISK MESSAGE
                # --------------------------------------------

                if risk == "High":

                    st.error(
                        "🔴 High predicted risk based on the "
                        "machine-learning model."
                    )

                elif risk == "Moderate":

                    st.warning(
                        "🟠 Moderate predicted risk based on "
                        "the machine-learning model."
                    )

                else:

                    st.success(
                        "🟢 Low predicted risk based on the "
                        "machine-learning model."
                    )


            # ------------------------------------------------
            # API ERROR
            # ------------------------------------------------

            else:

                st.error(
                    f"FastAPI returned status code "
                    f"{response.status_code}."
                )

                try:

                    st.json(response.json())

                except ValueError:

                    st.write(response.text)


        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Could not connect to the FastAPI backend. "
                "Please make sure your FastAPI server is running."
            )


        except requests.exceptions.Timeout:

            st.error(
                "⏱️ The request timed out. "
                "Please check whether the FastAPI server is responding."
            )


        except requests.exceptions.RequestException as error:

            st.error(
                f"An error occurred while communicating "
                f"with the backend: {error}"
            )


# ============================================================
# DISCLAIMER
# ============================================================

st.markdown(
    """
    <div class="disclaimer">
        <strong>⚠️ Important Notice</strong><br><br>
        HeartGuard AI is an educational and research prototype. Its results are model-generated estimates and are not a medical diagnosis.
        Always consult a qualified healthcare professional for medical advice, diagnosis, or treatment.
    </div>
    """,
    unsafe_allow_html=True
)