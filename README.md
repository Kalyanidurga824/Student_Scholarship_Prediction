# 🎓 Student Scholarship Prediction System

A Machine Learning-based web application that predicts whether a student is eligible for a scholarship based on academic performance, attendance, family income, and other eligibility criteria.

## 📌 Project Overview

The Student Scholarship Prediction System is designed to automate the scholarship screening process. By analyzing student details using a trained Machine Learning model, the system predicts whether a student is eligible for a scholarship, helping institutions save time and improve decision-making.

---

## ✨ Features

- Predicts student scholarship eligibility
- Simple and user-friendly interface
- Machine Learning-based prediction
- Displays prediction result with confidence score
- Fast and efficient prediction system

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📊 Dataset Features

The prediction model uses the following student information:

- CGPA
- Attendance
- Family Income
- Backlogs
- Category (OC/BC/SC/ST)
- Semester
- Sports Participation (Yes/No)
- Extra Curricular Activities (Yes/No)

---

## 🎯 Eligibility Criteria

The prediction considers factors such as:

- CGPA ≥ 7.5
- Attendance ≥ 75%
- Family Income ≤ ₹3,00,000
- No Active Backlogs
- Semester between 1 and 8
- Sports Participation (Bonus)
- Extra Curricular Activities (Bonus)

---

## 🤖 Machine Learning Model

- Algorithm: **Random Forest Classifier**
- Data Preprocessing
- Label Encoding
- Train-Test Split
- Model Training
- Prediction Generation

---

## 📂 Project Structure

```
Student_Scholarship_Prediction_System/
│
├── app.py
├── model/
│   ├── scholarship_model.pkl
│   ├── label_encoder.pkl
│   └── train_model.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── dataset/
│   └── scholarship_dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Kalyanidurga824/Student_Scholarship_Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Student_Scholarship_Prediction
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open Your Browser

```
http://127.0.0.1:5000
```

---

## 🔄 Project Workflow

1. Enter student details through the web interface.
2. Submit the form.
3. Flask processes the input data.
4. The Random Forest model predicts scholarship eligibility.
5. The prediction result and confidence score are displayed.

---

## 📦 Required Libraries

- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib

Install manually if needed:

```bash
pip install flask pandas numpy scikit-learn joblib
```

---

## 🚀 Future Enhancements

- Student Login System
- Admin Dashboard
- MySQL Database Integration
- Multiple Scholarship Categories
- Email Notifications
- PDF Report Generation
- Cloud Deployment

---

