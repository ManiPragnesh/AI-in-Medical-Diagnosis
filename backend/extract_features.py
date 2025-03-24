import os
import pandas as pd
import json
import logging

# Setup
DATASET_DIR = "backend/datasets"
FEATURE_DIR = "backend/features"
os.makedirs(FEATURE_DIR, exist_ok=True)

logging.basicConfig(level=logging.INFO)

# Feature extraction
def extract_features(disease, filename):
    path = os.path.join(DATASET_DIR, filename)
    if not os.path.exists(path):
        logging.warning(f"Dataset not found: {path}")
        return
    data = pd.read_csv(path)
    features = list(data.columns[:-1])
    feature_path = os.path.join(FEATURE_DIR, f"{disease}_features.json")
    with open(feature_path, "w") as f:
        json.dump(features, f, indent=4)
    logging.info(f"Features extracted for {disease} and saved to {feature_path}")

# Run for all datasets
datasets = {
    "diabetes": "diabetes.csv",
    "heart": "heart_disease.csv",
    "knee_joint": "knee_joint.csv",
    "liver": "liver.csv",
    "muscle": "muscle.csv",
    "respiratory": "respiratory.csv",
    "skin": "skin.csv"
}

for disease, file in datasets.items():
    extract_features(disease, file)