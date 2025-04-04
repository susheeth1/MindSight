# 🧠 MindSight – Mental Health Assessment Web App

**MindSight** is a web-based mental health screening tool that helps users self-assess their levels of **stress**, **anxiety**, and **depression** using a short, guided questionnaire based on DASS (Depression Anxiety Stress Scales). It uses machine learning models to predict the severity level for each condition.

---

## 🌟 Features

- 21-question assessment (7 for each: Stress, Anxiety, Depression)
- SVM-based machine learning models for prediction
- Severity levels: `Normal`, `Mild`, `Moderate`, `Severe`, `Extremely Severe`
- User-friendly UI built with HTML/CSS
- Backend powered by Python Flask
- Results displayed with personalized color-coded indicators

---

## 🚀 Tech Stack

| Frontend  | Backend | ML | Others |
|-----------|---------|----|--------|
| HTML, CSS | Flask   | scikit-learn, SVM | joblib, numpy |

---

## 📸 Screenshots

> Add screenshots here if needed using:
> `![Alt Text](path/to/screenshot.png)`

---

## 📦 Installation Instructions

### 1. Clone the repository

```bash
git clone https://github.com/susheeth1/MindSight.git
cd MindSight
```
2. Set up a virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run the app
```
python app.py
```
Then open your browser and go to: http://127.0.0.1:5000

📊 Severity Levels
Level	Label (Output)
1	Normal
2	Mild
3	Moderate
4	Severe
5	Extremely Severe

💡 Disclaimer
This app is intended for educational and demonstration purposes only. It is not a diagnostic tool. If you're experiencing mental health concerns, please consult a certified healthcare professional.

