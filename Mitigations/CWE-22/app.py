from flask import Flask, request, send_file, abort
import os

app = Flask(__name__)
BASE_DIR = "/app/configs" 

@app.route("/get-config", methods=["GET"])
def get_config():
    filename = request.args.get("file")
    if not filename:
        return "Missing filename", 400

    filepath = os.path.abspath(os.path.join(BASE_DIR, filename))

    if not filepath.startswith(BASE_DIR):
        return "Unauthorized access", 403

    if not os.path.exists(filepath):
        return "File not found", 404

    return send_file(filepath)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
