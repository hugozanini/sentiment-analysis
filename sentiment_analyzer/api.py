from typing import Dict

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .classifier.model import Model, get_model

app = FastAPI()

#Allowing CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    text:str

class SentimentResponse(BaseModel):
    probabilities: Dict[str, float]
    sentiment: str
    confidence: float


@app.post("/predict", response_model = SentimentResponse)
def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    '''
    The injection of the parameter model is done by the function get_model
    '''
    sentiment, confidence, probabilities = model.predict(request.text)
    return SentimentResponse(
        sentiment = sentiment,
        confidence = confidence,
        probabilities = probabilities
    )


#http POST http://127.0.0.1:8000/predict text="Test"
#bin/start_server