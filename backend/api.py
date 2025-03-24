from flask import Flask, request, jsonify
import joblib
import json
import os

app = Flask(__name__)

MODEL_DIR = "backend/models"
FEATURE_DIR = "backend/features"

def load_model(disease):
    model_path = os.path.join(MODEL_DIR, f"{disease}.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file '{model_path}' not found.")
    return joblib.load(model_path)

@app.route("/features/<disease>", methods=["GET"])
def get_features(disease):
    feature_path = os.path.join(FEATURE_DIR, f"{disease}_features.json")
    if not os.path.exists(feature_path):
        return jsonify({"error": "Features not found"}), 404
    with open(feature_path, "r") as f:
        features = json.load(f)
    return jsonify(features)

@app.route("/predict/<disease>", methods=["POST"])
def predict(disease):
    feature_path = os.path.join(FEATURE_DIR, f"{disease}_features.json")
    
    try:
        model = load_model(disease)

        if not os.path.exists(feature_path):
            return jsonify({"error": "Feature list not found"}), 404
        
        with open(feature_path, "r") as f:
            features = json.load(f)

        data = request.get_json()

        input_values = [float(data.get(feature, 0)) for feature in features]
        prediction = model.predict([input_values])[0]

        return jsonify({"prediction": str(prediction)})

    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except KeyError as e:
        return jsonify({"error": f"Missing input data: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid input format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
