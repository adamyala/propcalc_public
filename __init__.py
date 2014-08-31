from flask import Flask, render_template, request, g
app = Flask(__name__)

import inspect, os
app.database = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/propcalc.db'
import sqlite3
def connect_to_database():
	return sqlite3.connect(app.database)

@app.route("/")
def main():
	g.db = connect_to_database()
	current = g.db.execute('select * from subjects')
	subjects = current.fetchall()
	return render_template('my_properties.html', subjects=subjects)

import ast
@app.route("/edit_property/<subject>")
def edit_property(subject):
	subject = ast.literal_eval(subject)
	return render_template('edit_property.html', subject=subject)

from lib.prop_calc import *
@app.route('/sales_approach/<subject>', methods=['GET', 'POST'])
@app.route('/sales_approach/', defaults={'subject': None}, methods=['GET', 'POST'])
def sales_approach(subject):
	if request.method == 'POST':
		subject = {}
		for field in request.form:
			subject[field] = request.form[field]
		subject['address'] = subject['street'] + ' ' + subject['city'] + ', ' + subject['state'] + ' ' + subject['zipcode']
		subject['dlrs_sqft'] = round(float(subject['price']) / float(subject['impr_sqft']),2)
		subject['built'] = 2014 - int(subject['age'])
	else:
		subject = ast.literal_eval(subject)
	print subject
	print "we got here"
	comps = find_comps(subject['address'], float(subject['impr_sqft']), float(subject['price']), float(subject['age']), subject['use'], subject['level'], subject['condition'])
	return render_template('sales_approach.html', **locals())

@app.route("/income_approach/<subject>")
def income_approach(subject):
	subject = ast.literal_eval(subject)
	return render_template('income_approach.html', subject=subject)

@app.route("/cost_approach/<subject>")
def cost_approach(subject):
	return render_template('cost_approach.html', subject=subject)

if __name__ == "__main__":
	app.debug = True
	app.run()