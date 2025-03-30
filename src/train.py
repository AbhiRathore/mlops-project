import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os 
import yaml
import pickle
# Load Data


# Load MLflow config from YAML
with open("mlflow_config.yaml", "r") as f:
    config = yaml.safe_load(f)

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

X_train, y_train = train.drop(columns=["Outcome"]), train["Outcome"]
X_test, y_test = test.drop(columns=["Outcome"]), test["Outcome"]
print("hello")

# Enable MLflow Tracking
# Set MLflow tracking URI
mlflow.set_tracking_uri(config["mlflow_tracking_uri"])

# Create or set the experiment
mlflow.set_experiment(config["experiment_name"])

with mlflow.start_run():
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    preds = model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)

    # Ensure the directory exists
    os.makedirs("../models", exist_ok=True)

    # Save the trained model
    with open("../models/model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "logistic_model")
    
    print(f"Model trained and logged with accuracy: {accuracy}")

print(f"Model saved in MLflow under experiment: {config['experiment_name']}")

