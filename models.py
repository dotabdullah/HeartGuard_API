from pydantic import BaseModel, ConfigDict

class PatientData(BaseModel):
    model_config = ConfigDict(extra="forbid")

    age: int
    sex: int
    chest_pain_type: int
    resting_bp: int
    cholesterol: int
    fasting_bs: int
    resting_ecg: int
    max_heart_rate: int
    exercise_angina: int
    oldpeak: float
    st_slope: int
    cardiac_risk: int
    thallium_stress_test: int