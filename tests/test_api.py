from simple_text_api.db.models import TextAnalysisResult


# CLEAN TEXT ENDPOINT
def test_health_happy_path(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"Status": "OK"}


def test_clean_text_happy(test_client):
    payload = {"input_string": "machine learning is super"}
    response = test_client.post("/clean_text", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["clean_text"]


def test_clean_text_too_long(test_client):
    payload = {"input_string": "long input" * 1000}
    response = test_client.post("/clean_text", json=payload)
    assert response.status_code == 422


def test_clean_text_empty(test_client):
    payload = {"input_string": ""}
    response = test_client.post("/clean_text", json=payload)
    assert response.status_code == 422


def test_clean_text_one_space(test_client):
    payload = {"input_string": " "}
    response = test_client.post("/clean_text", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["clean_text"] == ""


# ANALYZE TEXT
def test_analyze_too_long(test_client):
    payload = {"input_string": "long input" * 1000}
    response = test_client.post("/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_empty(test_client):
    payload = {"input_string": ""}
    response = test_client.post("/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_whole(test_client, db_session):
    """
    Function tests API endpoint and saving result to DB
    """
    input: str = "Data Science! is grea@t"
    payload = {"input_string": input}
    response = test_client.post("/analyze", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["words_count"] == 4
    assert data["frequent_words"]
    assert data["frequent_chars"]
    assert data["original_text"] == input
    assert data["clean_text"] == "data science is great"

    query_result = db_session.query(TextAnalysisResult).all()
    assert query_result is not None
    assert len(query_result) == 1
    assert query_result[0].clean_text == "data science is great"
    assert query_result[0].id == 1
    assert query_result[0].words_count == 4
