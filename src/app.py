from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "AI-Based Student Performance Prediction Backend is Running!"

# Health check
@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "Server is running"
    })

# Predict endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    attendance = data.get("attendance")
    study_hours = data.get("study_hours")
    previous_grade = data.get("previous_grade")

    prediction = previous_grade + 5

    return jsonify({
        "attendance": attendance,
        "study_hours": study_hours,
        "previous_grade": previous_grade,
        "predicted_grade": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
