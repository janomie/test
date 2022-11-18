from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')

def hello_world():
    name = request.args.get('name')
    message = request.args.get('message')
    return 'Hello ' + name + '! ' + message

if __name__ == '__main__':
    app.run()