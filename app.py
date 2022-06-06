from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'codebaseBeta 2.0.0 says Hello, Docker!'
