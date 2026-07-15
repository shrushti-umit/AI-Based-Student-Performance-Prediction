from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    prompt = data.get("prompt")

    return jsonify({
        "response": f"You entered: {prompt}"
    })

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input data provided"}), 400

        input_data = pd.DataFrame([data])

        prediction = model.predict(input_data)

        return jsonify({
            "prediction": prediction[0]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
   
