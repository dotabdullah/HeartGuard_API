from pydantic import BaseModel, ConfigDict

class PatientData(BaseModel):

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


    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
                "example": {
                    "age": 55,
                    "sex": 1,
                    "chest_pain_type": 2,
                    "resting_bp": 140,
                    "cholesterol": 240,
                    "fasting_bs": 0,
                    "resting_ecg": 1,
                    "max_heart_rate": 150,
                    "exercise_angina": 0,
                    "oldpeak": 1.0,
                    "st_slope": 2,
                    "cardiac_risk": 1,
                    "thallium_stress_test": 2,
                }
            },
        )