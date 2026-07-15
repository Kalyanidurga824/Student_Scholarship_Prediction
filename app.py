from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# -------------------------------
# Load Model
# -------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "scholarship_model.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "category_encoder.pkl")

model = joblib.load(MODEL_PATH)
category_encoder = joblib.load(ENCODER_PATH)


# -------------------------------
# Home Page
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Prediction
# -------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        cgpa = float(request.form["cgpa"])
        attendance = int(request.form["attendance"])
        family_income = int(request.form["family_income"])
        backlogs = int(request.form["backlogs"])

        category = request.form["category"]
        semester = int(request.form["semester"])
        sports = int(request.form["sports"])
        extra = int(request.form["extra_activities"])

        category = category_encoder.transform([category])[0]

        student = np.array([[

            cgpa,
            attendance,
            family_income,
            backlogs,
            category,
            semester,
            sports,
            extra

        ]])

        prediction = model.predict(student)[0]

        probability = model.predict_proba(student)

        confidence = round(np.max(probability) * 100, 2)

        if prediction == 1:
            result = "Eligible for Scholarship"
        else:
            result = "Not Eligible for Scholarship"

        return render_template(
            "index.html",
            prediction=result,
            confidence=confidence
        )

    except Exception as e:

        return render_template(
            "index.html",
            prediction="Error",
            confidence=0,
            error=str(e)
        )


# -------------------------------
# Run App
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)