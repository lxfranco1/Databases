from flask import Flask, render_template, request
from Analyzer import Analyze

app = Flask(__name__)
app.debug=True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/team")
def about():
    return render_template("about.html")

@app.route("/output")
def output():
    return render_template("output.html")

@app.route("/input", methods=['POST', 'GET'])
def input():
    if request.method == 'GET':
        print("get")

    else:
        tweet_url = request.form['tweet_url']
        # get url that the user has entered
        Analyze(tweet_url)

    return render_template('input.html')

if __name__ == "__main__":
    app.run()
