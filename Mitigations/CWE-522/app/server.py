from flask import Flask, request, jsonify
import config  

import os

USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")

app = Flask(__name__)

@app.route("/get-credentials", methods=["GET"])
def get_credentials():
    return jsonify({"username": USERNAME, "password": PASSWORD})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
