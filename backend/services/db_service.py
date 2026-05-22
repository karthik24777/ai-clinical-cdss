from backend.database.database import SessionLocal, Patient

def save_prediction(symptoms: str, disease: str):
    db = SessionLocal()

    record = Patient(
        symptoms=symptoms,
        disease=disease
    )

    db.add(record)
    db.commit()
    db.close()