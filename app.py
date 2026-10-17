from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return {"message": "Hello, DevOps!"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)