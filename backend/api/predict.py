from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.predict_service import predict_disease
from backend.services.db_service import save_prediction

router = APIRouter()

class SymptomsRequest(BaseModel):
    symptoms: str

@router.post("/predict")
def predict(data: SymptomsRequest):

    disease = predict_disease(data.symptoms)

    # 💾 SAVE TO DATABASE
    save_prediction(data.symptoms, disease)

    return {
        "input_symptoms": data.symptoms,
        "predicted_disease": disease,
        "status": "saved to database"
    }