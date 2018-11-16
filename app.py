import os
from flask import Flask, request, render_template
app = Flask(__name__)

import json
import datetime 

app.config['DEBUG'] = True
import psycopg2
	
#conn = psycopg2.connect("dbname=farmtraining user=HemanthKondapalli password=Jrs92@")
#cur = conn.cursor()




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


@app.route('/signin')
def signin():
	'''
	Home page
	'''
	return render_template('signin.html')

@app.route('/fertilizers')
def fertilizers():
	'''
	Home page
	'''
	return render_template('fertilizers.html')

@app.route('/irrigation')
def irrigation():
	'''
	Home page
	'''
	return render_template('irrigation.html')

@app.route('/pesticide')
def pesticide():
	'''
	Home page
	'''
	return render_template('pesticide.html')

@app.route('/cropstorage')
def cropstorage():
	'''
	Home page
	'''
	return render_template('cropstorage.html')

@app.route('/financialliteracy')
def financialliteracy():
	'''
	Home page
	'''
	return render_template('financialliteracy.html')

@app.route('/croprotation')
def croprotation():
	'''
	Home page
	'''
	return render_template('croprotation.html')

@app.route('/fertilizers_quiz')
def fertilizersquiz():
	'''
	Home page
	'''
	return render_template('fertilizers_quiz.html')

@app.route('/irrigation_quiz')
def irrigationquiz():
	'''
	Home page
	'''
	return render_template('irrigation_quiz.html')

@app.route('/pesticide_quiz')
def pesticidequiz():
	'''
	Home page
	'''
	return render_template('pesticide_quiz.html')

@app.route('/crop_storage_quiz')
def cropstoragequiz():
	'''
	Home page
	'''
	return render_template('crop_storage_quiz.html')

@app.route('/financial_literacy_quiz')
def financialliteracyquiz():
	'''
	Home page
	'''
	return render_template('financial_literacy_quiz.html')

@app.route('/crop_rotation_quiz')
def croprotationquiz():
	'''
	Home page
	'''
	return render_template('crop_rotation_quiz.html')



@app.route('/quizresults', methods=['POST'])
def quizresults():
	'''
	Home page
	'''

	results = request.form
	score = 0

	if results.keys()[0][:2] == 'fl':
		lesson = "Financial Literacy"
		financial_literacy_solution = {"fl_q_2": "2", "fl_q_3": "3", "fl_q_1": "4", "fl_q_4": "4", "fl_q_5": "3"}
		for key in results.keys():
			if results[key] == financial_literacy_solution[key]:
				score += 1

	elif results.keys()[0][0] == 'p':
		lesson = "Pesticide"
		pesticide_solution = {"p_q_2": "3", "p_q_3": "4", "p_q_1": "2", "p_q_4": "4", "p_q_5": "3"}
		for key in results.keys():
			if results[key] == pesticide_solution[key]:
				score += 1
		
	elif results.keys()[0][0] == 'i':
		lesson = "Irrigation"
		irrigation_solution = {"i_q_2": "4", "i_q_3": "4", "i_q_1": "1", "i_q_4": "4", "i_q_5": "2"}
		for key in results.keys():
			if results[key] == irrigation_solution[key]:
				score += 1
		
	elif results.keys()[0][:2] == 'cr':
		lesson = "Crop Rotation"
		crop_rotation_solution = {"cr_q_2": "1", "cr_q_3": "4", "cr_q_1": "3", "cr_q_4": "1", "cr_q_5": "2"}
		for key in results.keys():
			if results[key] == crop_rotation_solution[key]:
				score += 1
		
	elif results.keys()[0][:2] == 'cs':
		lesson = "Crop Storage"
		crop_storage_solution = {"cs_q_2": "2", "cs_q_3": "4", "cs_q_1": "1", "cs_q_4": "1", "cs_q_5": "4"}
		for key in results.keys():
			if results[key] == crop_storage_solution[key]:
				score += 1

	elif results.keys()[0][0] == 'f':
		lesson = "Fertilizer"
		fertilizer_solution = {"f_q_2": "2", "f_q_3": "3", "f_q_1": "1", "f_q_4": "2", "f_q_5": "1"}
		for key in results.keys():
			if results[key] == fertilizer_solution[key]:
				score += 1
	
	print "phone number is {}".format(phonenumber)
	#cur.execute('INSERT INTO test_scores (phone_number, lesson, date, score)  VALUES (\'{}\', \'{}\', \'{}\', \'{}\');'.format(phonenumber, lesson, str(datetime.datetime.now()), score))
	#conn.commit()

	quiz_score = str(score)
	return render_template("quizresults.html", value = quiz_score)


@app.route('/user',methods = ['POST'])
def user():
	'''
	#Insert User
	cur.execute('INSERT INTO users (phone_number, name, state) VALUES (\'{}\', \'{}\', \'{}\');'.format(request.form["Phone"], request.form["Name"], request.form["State"] ))
	conn.commit()
	

	#Query Data for User Dashboard
	
	cur.execute('SELECT lesson, max(score) FROM test_scores WHERE phone_number = \'{}\' GROUP BY phone_number, lesson, date;'.format(request.form["Phone"]))
	results = cur.fetchall()
	'''
	global phonenumber
	phonenumber = request.form["Phone"]
	print "phone number in user is {}".format(phonenumber)
	return render_template('user.html')


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host='0.0.0.0', port=port)
