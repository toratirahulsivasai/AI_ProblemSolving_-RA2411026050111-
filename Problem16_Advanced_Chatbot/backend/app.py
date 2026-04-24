from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot_engine import get_response

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    response = get_response(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)