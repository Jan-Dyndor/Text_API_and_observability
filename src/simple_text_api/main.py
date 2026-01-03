from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check() -> dict:
    return {"Status": "OK"}
