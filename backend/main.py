from fastapi import FastAPI

from app.database.database import Base, engine
from app.models import user
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Sports Injury Risk Detection API"}