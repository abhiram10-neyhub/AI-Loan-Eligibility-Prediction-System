import pandas as pd
import os
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/loan_dataset.csv")

encoders = {}

categorical = [
    "Gender",
    "Married",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

for col in categorical:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

pred = model.predict(X)

print("Accuracy :", accuracy_score(y, pred))

joblib.dump(model, "models/loan_model.pkl")
joblib.dump(encoders, "models/label_encoders.pkl")

print("✅ AI Loan Model Trained Successfully!")