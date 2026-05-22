from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "secretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# fake doctor login (we will improve later)
fake_user = {
    "username": "doctor",
    "password": "admin123"
}

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_user(username, password):
    return username == fake_user["username"] and password == fake_user["password"]