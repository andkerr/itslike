from flask import Flask
from random import randrange

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {'response':"Flask is connected. We are live!!"}

@app.route('/random')
def return_random():
    return {
        'rand1': randrange(10),
        'rand2': randrange(10)
    }