from app import app

@app.route('/')
@app.route('/index')
def index():
    return "<h1>Hello, World!</h1>"

# #dynamic routes
# @app.route('/user/<name>')
# def user(name):
#     return "<h1>Hello, %!</h1>" % name
