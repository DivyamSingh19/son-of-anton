from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello flask"

if __name__=="__main__":
    app.run(debug=True)


@app.route("/analyze")
def analysis():
    return "Analysis route"

if __name__=="__main__":
 app.run(debug=True)