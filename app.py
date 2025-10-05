from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Hello from Devashish's Azure CI/CD demo! 🚀"

@app.route("/health")
def health():
    return jsonify(ok=True)
