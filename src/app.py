from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

@app.post("/predict/")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}
