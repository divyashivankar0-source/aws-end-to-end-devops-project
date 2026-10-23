
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AWS DevOps Project</h1>
    <p>My application is running successfully!</p>
    <p>Deployed using Docker, Jenkins and Kubernetes</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "aws-devops-app"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
