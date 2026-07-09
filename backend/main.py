from fastapi import FastAPI

app = FastAPI(
    title="Sports Injury Risk Detection API",
    version="1.0.0",
    description="Backend API for Sports Injury Risk Detection Platform"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Sports Injury Risk Detection API"
    }