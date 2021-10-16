from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {'response':"Flask is connected. We are live!!"}