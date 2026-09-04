from fastapi import FastAPI
import joblib
from models import PatientData
import pandas as pd
import sklearn
import json
import warnings
warnings.filterwarnings('ignore')


app = FastAPI(
    title="HeartGuard API",
    description="Heart Disease Risk Prediction API",
    version="1.0.0",
)

loaded_model = joblib.load("heartguard_ai.joblib")

# sample json data get
with open("sample_data.json", "r") as file:
    sample_patients = json.load(file)


@app.get("/")
def greet():
    return { "message": "HeartGuard AI API is running"}


@app.get("/health")
def health_check():
    return{
        "status": "healthy",
        "model": "HeartGuard AI Random Forest"
    }


@app.get("/sample-data")
def get_sample_data():
    return sample_patients

@app.post("/predict")
def make_prediction(patient: PatientData):
    
    patient_df = pd.DataFrame([patient.model_dump()])
    prediction = loaded_model.predict(patient_df)[0]
    probability = loaded_model.predict_proba(patient_df)[0][1]

    if probability >= 0.70:
        risk="High"
        message= "Model predicts elevated heart disease risk."
    elif probability >= 0.40:
        risk="Moderate"
        message= "Model predicts moderate heart disease risk."
    else:
        risk="Low"
        message= "Model predicts low heart disease risk."

    return{
        "prediction": int(prediction),
        "probability": probability,
        "risk": risk,
        "message": message
    }            

