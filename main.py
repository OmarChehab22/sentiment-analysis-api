from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import torch

# Initialize FastAPI app
app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple API for sentiment analysis using Hugging Face Transformers",
    version="1.0.0"
)

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextInput(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float

@app.get("/")
async def root():
    return {"message": "Welcome to the Sentiment Analysis API"}

@app.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(text_input: TextInput):
    try:
        # Get sentiment analysis result
        result = sentiment_analyzer(text_input.text)[0]
        
        return SentimentResponse(
            sentiment=result["label"],
            confidence=result["score"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 