from flask import request, url_for, Flask

app = Flask(__name__)


# ctx = app.test_request_context('/?next')
# ctx.push()


@app.route('/')
def index():
    pass


def redirect_url():
    return request.args.get('next') or request.referrer or url_for('index')


# print(redirect_url())
# ctx.pop()
with app.test_request_context('/?next'):
    print(redirect_url())


@app.teardown_request
def teardown_request(exception=None):
    print('this runs after request')


# ctx = app.test_request_context()
# ctx.push()
# ctx.pop()