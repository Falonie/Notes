from flask import Flask, url_for, request,redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello_world():
    return 'Hello,World!'


@app.route('/user/<string:username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# @app.route('/login/<username>', methods=['GET', 'POST'])
@app.route('/login/<string:username>')
def login(username):
    # if request.method == 'POST':
    #     pass
    # elif request.method == 'GET':
    #     return url_for('about')
    return 'Login %s' % username

@app.route('/other/')
def other():
    return redirect(url_for('index'))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('show_user_profile', username='Falonie Wang'))
if __name__ == '__main__':
    app.run(debug=True)
