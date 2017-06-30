from flask import redirect
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	return redirect('http://www.sina.com.cn')

@app.route('/hello')
def index1():
	response = make_response('<h1>This document carries a cookie</h1>')
	response.set_cookie('answer','42')
	return response

if __name__ == '__main__':
	app.run(debug=True)

