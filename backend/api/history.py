from fastapi import APIRouter
from backend.database.database import SessionLocal, Patient

router = APIRouter()

@router.get("/patients")
def get_patients():
    db = SessionLocal()

    patients = db.query(Patient).all()

    result = []

    for p in patients:
        result.append({
            "id": p.id,
            "symptoms": p.symptoms,
            "disease": p.disease
        })

    db.close()
    return result