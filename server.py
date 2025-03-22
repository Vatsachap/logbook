from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/names')
def names():
    return ["vatsa","bob","pap"]
@app.route('/hello/<name>')
def greetings(name):
    return f'Hello, {name}!

if __name__ == '__main__':
    app.run(host='', port=5000)  # Set host to '' to allow access from any IP address
    