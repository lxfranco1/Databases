from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.debug=True

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/input", methods=['POST', 'GET'])
def input():
    if request.method == 'GET':
        print("no")

    else:
        tweet_url = request.form['tweet_url']
        # get url that the user has entered
        r = requests.get(tweet_url)
        print(r.text)

    return render_template('input.html')

if __name__ == "__main__":
    app.run()
