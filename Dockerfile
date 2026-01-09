FROM python:3.12-slim 

WORKDIR /app
RUN mkdir -p /app/data

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src 

ENV PYTHONPATH=/app/src

EXPOSE 8000 

CMD ["uvicorn", "simple_text_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
