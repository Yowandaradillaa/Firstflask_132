from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<div>Hello World</div>"
@app.route('/salam')

def hello():
    return "Assalamualaikum"

