from flask import Flask, current_app

app = Flask(__name__)
# print(current_app.name)
with app.app_context():
    print(current_app.name)

ctx = app.app_context()
ctx.push()
print(current_app.name)
ctx.pop()

# if __name__ == '__main__':
