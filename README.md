# HeartGuard AI

## Solution Name

**HeartGuard AI - Heart Disease Risk Prediction System**

HeartGuard AI is an educational machine-learning application that estimates a patient's heart disease risk from demographic, vital, laboratory, exercise, ECG, and cardiac-test information.

> This project is for educational and demonstration purposes only. Its output is a model-based estimate, not a medical diagnosis or a substitute for professional medical advice.

## The Problem

Heart disease risk depends on multiple patient indicators rather than a single measurement. Reviewing these values together can be difficult in a simple form or manual workflow.

HeartGuard AI addresses this problem by providing a browser-based interface where users can enter patient data and receive a consistent prediction from a trained classification model. The system returns:

- A binary prediction indicating predicted heart disease or no heart disease
- The model probability for the positive class
- A risk category: Low, Moderate, or High
- A short explanatory status message

## The Machine Learning Core

The prediction engine is a serialized scikit-learn `RandomForestClassifier` stored in `backend/heartguard_ai.joblib`.

### Training approach

- Input features: 13 patient attributes
- Target: heart disease classification label
- Train/test split: 80/20
- Split strategy: stratified, with `random_state=42`
- Model: Random Forest with 100 estimators and `random_state=42`
- Probability output: `predict_proba()` for the positive class

The training script evaluates accuracy, balanced accuracy, precision, recall, F1 score, confusion matrix, classification report, ROC-AUC, and feature importance. The repository does not currently store the generated metric values, so results should be regenerated from the training script when reproducible benchmark numbers are required.

### Risk thresholds

The API maps the positive-class probability to a simple risk label:

| Probability | Risk |
|---|---|
| Less than 0.40 | Low |
| 0.40 to less than 0.70 | Moderate |
| 0.70 or higher | High |

## Tech Stack

- **Python**: Application and model runtime
- **FastAPI**: REST API backend
- **Pydantic**: Request validation and schema generation
- **Streamlit**: Interactive frontend
- **scikit-learn**: Random Forest model and evaluation metrics
- **pandas**: Patient input preparation and tabular data handling
- **joblib**: Model serialization and loading
- **Requests**: Frontend-to-backend HTTP communication
- **Uvicorn**: ASGI development server

## System Architecture

```text
+----------------------+       HTTP/JSON        +--------------------------+
| Streamlit frontend   | ---------------------> | FastAPI backend          |
| frontend/app.py      |                        | backend/main.py          |
+----------------------+                        +------------+-------------+
                                                            |
                                                            v
                                               +--------------------------+
                                               | Pydantic PatientData     |
                                               | validation               |
                                               +------------+-------------+
                                                            |
                                                            v
                                               +--------------------------+
                                               | Random Forest model      |
                                               | heartguard_ai.joblib     |
                                               +------------+-------------+
                                                            |
                                                            v
                                               +--------------------------+
                                               | Prediction, probability, |
                                               | risk, and message        |
                                               +--------------------------+
```

### Backend endpoints

- `GET /` - Confirms that the API is running
- `GET /health` - Returns backend and model health information
- `GET /sample-data` - Returns example patient records
- `POST /predict` - Validates patient data and returns a prediction

The API uses strict request validation. Extra fields are rejected by the `PatientData` schema.

### Run the project locally

From the project root, activate the virtual environment if needed:

```powershell
.\myenv\Scripts\Activate.ps1
```

Start the backend in one terminal:

```powershell
cd backend
uvicorn main:app --reload
```

Start the Streamlit frontend in a second terminal:

```powershell
cd frontend
streamlit run app.py
```

The API is available at `http://127.0.0.1:8000` and the Streamlit interface will display its local URL in the terminal.

## Performance

### Runtime characteristics

- The model is loaded once when the FastAPI application starts.
- Each prediction performs request validation, creates a one-row pandas DataFrame, and runs Random Forest inference in-process.
- No database or external model service is required for inference.
- The `/health` endpoint provides a quick availability check for the backend and loaded model.

### Evaluation and limitations

The training script includes standard classification metrics and ROC-AUC for offline evaluation. Actual accuracy, latency, throughput, and memory measurements are not committed to this repository and should be benchmarked in the target deployment environment.

Performance can vary based on hardware, Python and library versions, server workers, concurrent requests, and the size of the deployed model. The current setup is appropriate for a small educational application and should be load-tested before production use.

## Project Structure

```text
backend/
  heartguard_ai.joblib       Trained Random Forest model
  main.py                    FastAPI application
  models.py                  Pydantic request model
  sample_data.json           Example patient inputs
frontend/
  app.py                     Streamlit application
  old_app.py                 Earlier frontend version
model training/
  heartguard_ai_heart_disease_risk_prediction.py  Training and evaluation script
  HeartGuard_AI_Heart_Disease_Risk_Prediction.ipynb  Training notebook
```
