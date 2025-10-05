from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def root():
    return "OK"

@app.route("/health")
def health():
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
