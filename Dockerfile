FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY  src/* .
COPY models/model.pkl .
COPY mlflow_config.yaml .

CMD ["python", "train.py"]
