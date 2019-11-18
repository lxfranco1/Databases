from flask import Flask
from Analyzer import Analyze
app = Flask(__name__)


@app.route("/")
def home():
    Analyze()
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
