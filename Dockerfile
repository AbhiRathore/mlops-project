FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY  src/* .
COPY models/model.pkl .
COPY mlflow_config.yaml .
# Expose FastAPI port
EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

