from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name + '</string:name>'

def error(raise_):
    if raise_:
        raise ValueError('Raised the error!')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')