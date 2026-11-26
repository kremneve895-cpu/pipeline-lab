from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "pipeline-lab demo app"}

@app.route("/health")
def health():
    return {"status": "ok"}
