from flask import Flask

app = Flask(__name__)


@app.route('/f/<celsius>')
def convert_c_to_f(celsius=100):
    """Convert celsius to fahrenheit"""
    fahrenheit = float(celsius) * 9 / 5 + 32
    return str(fahrenheit)


if __name__ == '__main__':
    app.run()
