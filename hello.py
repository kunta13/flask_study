from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<h1>Your browser is %s</h1>' % user_agent
@app.route('/hello')
def hello():
	return '<h2>hello da</h2>'

@app.route('/user/<name>')
def user(name):
	return '<h1>hello,%s!</h1>' % name
if __name__ == '__main__':
	app.run(debug=True)

