from fastapi import FastAPI
from app.schemas.user import UserCreate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"message": "Health endpoint"}

@app.post("/ping/")
def ping(user: UserCreate):
    return {"message": user}