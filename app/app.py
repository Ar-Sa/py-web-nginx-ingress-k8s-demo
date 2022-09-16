from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2> All Well </h2>"

# Dummy for liveness and readiness probes
@app.route("/health")
def health():
    return 'OK'

