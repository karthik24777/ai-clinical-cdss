from fastapi import APIRouter
from backend.services.speech_to_text import listen_and_convert
from backend.services.predict_service import predict_disease

router = APIRouter()

@router.get("/voice-predict")
def voice_predict():
    # Step 1: Convert speech → text
    symptoms_text = listen_and_convert()

    # Step 2: Predict disease using ML model
    result = predict_disease(symptoms_text)

    return {
        "voice_input": symptoms_text,
        "predicted_disease": result
    }