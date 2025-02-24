from flask import Flask, jsonify
from flask_cors import CORS  # Import this
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Add this line, it allows your frontend to communicate with backend

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask server running!"})

@app.route("/api/hello", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
