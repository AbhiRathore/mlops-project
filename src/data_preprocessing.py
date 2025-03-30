import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data():
    df = pd.read_csv("https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv")
    df.columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
    
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    train.to_csv("train.csv", index=False)
    test.to_csv("test.csv", index=False)
    
    print("Data preprocessing complete.")

if __name__ == "__main__":
    preprocess_data()
