import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models/model.pkl")

model = pickle.load(open(model_path, "rb"))

def predict_disease(symptoms):

    # 🛡️ SAFETY CHECK (VERY IMPORTANT)
    if symptoms is None:
        return "No symptoms provided"

    if not isinstance(symptoms, str):
        symptoms = str(symptoms)

    symptoms = symptoms.strip()

    if symptoms == "":
        return "Empty symptoms input"

    # 🧠 Prediction
    prediction = model.predict([symptoms])[0]

    return prediction