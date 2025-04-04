# 🧠 MindSight – Mental Health Assessment Web App ( Mental-health-and-well-being-surveillance-assessment-and-tracking-solution-among-children.(Presidency Univerity Final year project ISR-G03) )

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
> ![home(1)](https://github.com/user-attachments/assets/529adeca-0272-4be1-a1d4-6526d83877ad)
> ![Stress(2)](https://github.com/user-attachments/assets/d06d9341-6da4-4756-9633-3b398e13f9bf)
> ![Stress(3)](https://github.com/user-attachments/assets/913f3f35-dfe8-41c1-99c8-a3e7845cde15)
> ![Anxiety(4)](https://github.com/user-attachments/assets/0daf5b18-894c-4cd3-af5f-aa89c15867e0)
> ![Anxiety(5)](https://github.com/user-attachments/assets/730190e4-9cd3-4f1f-b617-d8d4d89e71ca)
> ![Depressin(6)](https://github.com/user-attachments/assets/bb0d191c-a761-49a1-a1ef-6ec6b85a7951)
> ![Depression(7)](https://github.com/user-attachments/assets/6a29a685-6109-4fd9-818d-532c9024be38)
> ![Result(8)](https://github.com/user-attachments/assets/8081fd45-0b87-4d81-9467-44730e641560)
> ![Result(9)](https://github.com/user-attachments/assets/227e1a78-5d14-454a-a8ee-9ee37188c8f7)

---
### Team Members
| Sl. No. | Roll Number     | Student Name        |
|---------|-----------------|---------------------|
| 1       | 20211ISR0036    | Susheeth G          |
| 2       | 20211ISR0047    | Ritish N            |
| 3       | 20211ISR0039    | Vidyashree BN       |
| 4       | 20211ISR0082    | Mithali S Anand     |
| 5       | 20211ISR0040    | Tejashwini BA       |
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

