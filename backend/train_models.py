import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import logging

# Setup
DATASET_DIR = "backend/datasets"
MODEL_DIR = "backend/models"
os.makedirs(MODEL_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)

def train_model(disease, path):
    data = pd.read_csv(path)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))
    logging.info(f"{disease.capitalize()} Model Accuracy: {accuracy}")

    joblib.dump(model, os.path.join(MODEL_DIR, f"{disease}.pkl"))

datasets = {
    "diabetes": "backend/datasets/diabetes.csv",
    "heart": "backend/datasets/heart_disease.csv"
}

for disease, path in datasets.items():
    train_model(disease, path)