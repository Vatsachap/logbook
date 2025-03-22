from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/names')
def names():
    return ["vatsa","bob","pap"]

if __name__ == '__main__':
    app.run(host='', port=5000)  # Set host to '' to allow access from any IP address
    