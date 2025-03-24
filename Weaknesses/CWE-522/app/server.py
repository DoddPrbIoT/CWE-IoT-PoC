from flask import Flask, request, jsonify
import config  

app = Flask(__name__)

@app.route("/get-credentials", methods=["GET"])
def get_credentials():
    return jsonify({"username": config.USERNAME, "password": config.PASSWORD})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
