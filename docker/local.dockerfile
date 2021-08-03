FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY .. /app

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 80 --reload
