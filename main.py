from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import numpy as np

# Load model at startup
model_data = joblib.load("model.pkl")
model = model_data["model"]
features = model_data["features"]
mse = model_data["mse"]
r2 = model_data["r2"]

app = FastAPI(
    title="House Price Prediction API",
    description="Predicts house prices based on square footage, bedrooms, bathrooms, and age.",
    version="1.0"
)

# Input schema
class PredictionInput(BaseModel):
    square_feet: float = Field(..., example=2000)
    bedrooms: int = Field(..., example=3)
    bathrooms: int = Field(..., example=2)
    age: int = Field(..., example=10)

# Output schema
class PredictionOutput(BaseModel):
    predicted_price: float

@app.get("/")
def health_check():
    return {"status": "healthy", "message": "House Price Prediction API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    try:
        features_array = np.array([[ 
            input_data.square_feet, 
            input_data.bedrooms, 
            input_data.bathrooms, 
            input_data.age 
        ]])
        prediction = model.predict(features_array)[0]
        
        return PredictionOutput(predicted_price=float(prediction))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/model-info")
def model_info():
    return {
        "model_type": type(model).__name__,
        "problem_type": "regression",
        "features": features,
        "mse": mse,
        "r2_score": r2
    }
