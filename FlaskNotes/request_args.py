from flask import Flask, current_app,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return request.headers


if __name__ == '__main__':
    app.run()
