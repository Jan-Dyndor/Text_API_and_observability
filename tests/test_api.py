from fastapi.testclient import TestClient

from simple_text_api.main import app

client = TestClient(app)


# CLEAN TEXT ENDPOINT
def test_health_happy_path():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"Status": "OK"}


def test_clean_text_happy():
    payload = {"input_string": "machine learning is super"}
    response = client.post("/clean_text", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["clean_text"]


def test_clean_text_too_long():
    payload = {"input_string": "long input" * 1000}
    response = client.post("/clean_text", json=payload)
    assert response.status_code == 422


def test_clean_text_empty():
    payload = {"input_string": ""}
    response = client.post("/clean_text", json=payload)
    assert response.status_code == 422


def test_clean_text_one_space():
    payload = {"input_string": " "}
    response = client.post("/clean_text", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["clean_text"] == ""


# ANALYZE TEXT
def test_analyze_too_long():
    payload = {"input_string": "long input" * 1000}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_empty():
    payload = {"input_string": ""}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_whole():
    input: str = "Data Science! is grea@t"
    payload = {"input_string": input}
    response = client.post("/analyze", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["words_count"] == 4
    assert data["frequent_words"]
    assert data["frequent_chars"]
    assert data["original_text"] == input
    assert data["clean_text"] == "data science is great"
