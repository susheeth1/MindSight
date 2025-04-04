from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load trained models (no scaler needed)
model_dir = os.path.join(os.path.dirname(__file__), 'models')

stress_model = joblib.load(os.path.join(model_dir, "svm_stress_model.pkl"))
anxiety_model = joblib.load(os.path.join(model_dir, "svm_anxiety_model.pkl"))
depression_model = joblib.load(os.path.join(model_dir, "svm_depression_model.pkl"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/assessment')
def assessment():
    return render_template("assessment.html")

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('responses')
    
    if not data or len(data) != 21:
        return jsonify({'error': 'Expected 21 responses'}), 400

    # Extract sub-sections
    stress_input = np.array(data[:7]).reshape(1, -1)
    anxiety_input = np.array(data[7:14]).reshape(1, -1)
    depression_input = np.array(data[14:]).reshape(1, -1)

    # Compute scores (sum of 7 questions each)
    stress_score = sum(data[:7])
    anxiety_score = sum(data[7:14])
    depression_score = sum(data[14:])

    # Predict using models
    stress_pred = int(stress_model.predict(stress_input)[0])
    anxiety_pred = int(anxiety_model.predict(anxiety_input)[0])
    depression_pred = int(depression_model.predict(depression_input)[0])

    return jsonify({
        "stress_score": stress_score,
        "anxiety_score": anxiety_score,
        "depression_score": depression_score,
        "stress_level": map_level(stress_pred),
        "anxiety_level": map_level(anxiety_pred),
        "depression_level": map_level(depression_pred)
    })

def map_level(code):
    return {
        1: "Normal",
        2: "Mild",
        3: "Moderate",
        4: "Severe",
        5: "Extremely Severe"
    }.get(code, "Unknown")

if __name__ == '__main__':
    app.run(debug=True)
