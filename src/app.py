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
   
