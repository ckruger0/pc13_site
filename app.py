import os
from flask import Flask, request, render_template
app = Flask(__name__)



@app.route('/')
def index():
	'''
	Home page
	'''
	return render_template('index.html')

@app.route('/signup')
def submit():
	'''
	Home page
	'''
	return render_template('signup.html')

@app.route('/user')
def user():
	'''
	Home page
	'''
	return render_template('user.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)