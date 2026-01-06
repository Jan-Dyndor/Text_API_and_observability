from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from simple_text_api.db.database import Base, engine
from simple_text_api.schemas.schemas import AnalyzeResponse, CleanRequest, CleanResponse
from simple_text_api.services.clean_text import clean_input
from simple_text_api.services.text_analysis import (
    count_sentences,
    count_words,
    most_frequent_char,
    most_frequent_words,
)
from simple_text_api.db.database import get_db
from simple_text_api.db.models import TextAnalysisResult
import json


Base.metadata.create_all(bind=engine)  # Create table

app = FastAPI()


@app.get("/health")
def health_check() -> dict:
    return {"Status": "OK"}


@app.post("/clean_text", response_model=CleanResponse)
def clean_text(text: CleanRequest) -> CleanResponse:
    clean = clean_input(text.input_string)
    return CleanResponse(clean_text=clean)


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(text: CleanRequest, db: Session = Depends(get_db)) -> AnalyzeResponse:
    clean_str = clean_input(text.input_string)
    words_count = count_words(clean_str)
    sentence_count = count_sentences(clean_str)
    frequent_words = most_frequent_words(clean_str)
    frequent_chars = most_frequent_char(clean_str)

    db_obj = TextAnalysisResult(
        original_text=text.input_string,
        clean_text=clean_str,
        words_count=words_count,
        sentence_count=sentence_count,
        frequent_words_json=json.dumps(frequent_words),
        frequent_chars_json=json.dumps(frequent_chars),
    )
    try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
    except Exception as e:
        db.rollback()
        print(f"Issue occured while saving to DB {e}")
        raise HTTPException(status_code=500, detail="Database error")

    return AnalyzeResponse(
        words_count=words_count,
        sentence_count=sentence_count,
        frequent_words=frequent_words,
        frequent_chars=frequent_chars,
        original_text=text.input_string,
        clean_text=clean_str,
    )
