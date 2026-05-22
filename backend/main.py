from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.login import router as login_router
# APIs
from backend.api.predict import router as predict_router
from backend.api.voice_predict import router as voice_router
from backend.api.history import router as history_router

app = FastAPI(title="AI Clinical CDSS")

# CORS (frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home route
@app.get("/")
def home():
    return {"message": "AI Clinical CDSS Backend is running"}

# Register APIs
app.include_router(predict_router)
app.include_router(voice_router)
app.include_router(history_router)
app.include_router(login_router)