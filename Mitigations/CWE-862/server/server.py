from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

device_status = {"on": False}


@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad credentials"}), 401

@app.route('/api/device/on', methods=['POST'])
@jwt_required()
def turn_on_device():
    device_status["on"] = True
    return jsonify({"message": "Device turned ON!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
