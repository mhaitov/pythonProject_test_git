from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'

@app.route('/home')
def home():
    return 'Hello this is admin page '



@app.route('<not_found>')
def user(not_found):
    return f'Hello, page {not_found}, was not found'


@app.route('/<usr>')
def user(usr):
    return f'Hello{usr}'


@app.route('/about')
def about():
    return 'About me'

@app.route('/contact')
def contact():
    return 'My email is bob@example.com'

if __name__ == '__main__':
    app.run()

