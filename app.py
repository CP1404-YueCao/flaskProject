from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)<h1>'


@app.route('/greet')
def greet():
    return 'Hello'


@app.route('/greet/<name>')
def greeting(name=""):
    return "Hello {}".format(name)


if __name__ == '__main__':
    app.run()
