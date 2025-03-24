import os
from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_CREDENTIALS = {
    "username": os.getenv("APP_USERNAME"),
    "password": os.getenv("APP_PASSWORD")
}

sensor_data_db = []

@app.route('/upload', methods=['POST'])
def upload_data():
    auth = request.authorization

    if not auth or auth.username != VALID_CREDENTIALS["username"] or auth.password != VALID_CREDENTIALS["password"]:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    sensor_data_db.append(data)
    return jsonify({"message": "Data received successfully"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(sensor_data_db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
