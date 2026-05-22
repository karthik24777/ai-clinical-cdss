from fastapi import APIRouter
from pydantic import BaseModel
from backend.auth.auth_handler import verify_user, create_token

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if verify_user(data.username, data.password):
        token = create_token({"user": data.username})
        return {"access_token": token}
    
    return {"error": "Invalid credentials"}