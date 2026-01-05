# Text Processing API

A lightweight backend service built with **FastAPI** that provides basic text processing utilities (cleaning and analysis) and stores request history in a database.  
This project is intentionally small and practical — designed to strengthen Python backend fundamentals (project structure, API design, validation, testing, Docker, and persistence).

---

## Goals

- Build a clean, maintainable **Python backend** using FastAPI
- Practice **API design** (request/response schemas, error handling)
- Add **persistence** (store analysis results in a database)
- Write **automated tests** (pytest)
- Containerize the service with **Docker**

---

## Features

### 1) Health Check

- Simple endpoint to verify the service is running.

### 2) Text Cleaning

- Normalize and clean text using deterministic rules (no ML).
- Example operations:
  - lowercasing
  - trimming whitespace
  - removing punctuation / special characters
  - collapsing multiple spaces

### 3) Text Analysis

- Compute basic statistics from a given text, e.g.:
  - character count
  - word count
  - sentence count (simple heuristic)
  - most frequent words (optional)

### 4) Persistence (Database)

- Store each processed request/response so the user can inspect history.
- Database can be **SQLite** for local development.

---

## API Endpoints (planned)

### `GET /health`

Returns service status.
**Response**

```json
{ "status": "ok" }
```

### `POST / clean`

**Request**

```json
{ "text": "Some TEXT!!!  " }
```

**Response**

```json
{ "status": "ok" }
```

### 'POST / analyze'

**Request**

```json
{ "text": "Hello world. Hello again!" }
```

**Response**

```json
{
  "text": "Hello world. Hello again!",
  "char_count": 25,
  "word_count": 4,
  "sentence_count": 2,
  "top_words": [
    { "word": "hello", "count": 2 },
    { "word": "world", "count": 1 },
    { "word": "again", "count": 1 }
  ]
}
```

The project uses unit tests for pure text-processing logic and integration tests for FastAPI endpoints with a test SQLite database using dependency overrides.
