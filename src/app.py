from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

chat_history = []

model = joblib.load("model.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        input_data = pd.DataFrame([data])

        prediction = model.predict(input_data)

        chat_history.append({
            "input": data,
            "prediction": float(prediction[0])
        })

        return jsonify({
            "prediction": float(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/history", methods=["GET"])
def history():
    return jsonify(chat_history)


if __name__ == "__main__":
    app.run(debug=True)
