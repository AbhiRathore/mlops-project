mlops-project/
│── .github/workflows/mlops-ci.yml   # GitHub Workflow for CI/CD
│── src/
│   ├── data_preprocessing.py        # Data processing script
│   ├── train.py                      # Model training script
│── models/
│   ├── model.pkl                     # Stored model (tracked via MLflow)
│── requirements.txt
│── Dockerfile                        # Containerize model for deployment
│── mlflow_config.yaml                 # MLflow configuration
│── README.md
