from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated IoT device control
device_status = {"on": False}

@app.route('/api/device/on', methods=['POST'])
def turn_on_device():
    device_status["on"] = True
    return jsonify({"message": "Device turned ON!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
