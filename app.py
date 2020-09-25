from flask import Flask

app = Flask(__name__)


@app.route('/dawn')
def hello_world():
    return 'New Dawn, New Day!'


if __name__ == '__main__':
    app.run()
