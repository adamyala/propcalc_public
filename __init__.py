from flask import Flask, render_template, request, g
app = Flask(__name__)

app.database = '../propcalc/propcalc.db'
import sqlite3
def connect_to_database():
	return sqlite3.connect(app.database)

@app.route("/")
def main():
	g.db = connect_to_database()
	current = g.db.execute('select * from subjects')
	# subjects = [dict(owner=row[0], pin=row[1], pin=row[2]) for row in current.fetchall()]
	subjects = current.fetchall()
	return render_template('my_properties.html', subjects=subjects)

import ast
@app.route("/edit_property/<subject>")
def edit_property(subject):
	subject = ast.literal_eval(subject)
	return render_template('edit_property.html', subject=subject)

from lib.prop_calc import *
@app.route("/sales_approach/", methods=['GET', 'POST'])
def sales_approach():
	if request.method == 'POST':
		subject = [''] * 15
		# owner
		subject[0] = request.form['owner']
		# street
		subject[1] = request.form['street']
		# city 
		subject[2] = request.form['city']
		# state
		subject[3] = request.form['state']
		# zipcode
		subject[4] = request.form['zipcode']
		# impr_sqft
		subject[5] = request.form['impr_sqft']
		# land_sqft
		subject[6] = request.form['land_sqft']
		# price
		subject[7] = request.form['price']
		# age
		subject[8] = request.form['age']
		# use
		subject[9] = request.form['use']
		# level
		subject[10] = request.form['level']
		# condition
		subject[11] = request.form['condition']
		# address
		subject[12] = subject[1] + ' ' + subject[2] + ', ' + subject[3] + ' ' + subject[4]
		# dlrs_sqft
		subject[13] = round(float(subject[7]) / float(subject[5]),2)
		# built
		subject[14] = 2014 - int(subject[8])
		# sales_approach(address, impr_sqft, price, age, use, level, condition)
		comps = find_comps(subject[12], float(subject[5]), float(subject[7]), float(subject[8]), subject[9], subject[10], subject[11])
	return render_template('sales_approach.html', **locals())

@app.route("/sales_approach_2/<subject>")
def sales_approach_2(subject):
	# sales_approach(address, impr_sqft, price, age, use, level, condition)
	subject = ast.literal_eval(subject)
	comps = find_comps(subject[12], float(subject[5]), float(subject[7]), float(subject[8]), subject[9], subject[10], subject[11])
	return render_template('sales_approach_2.html', **locals())

@app.route("/income_approach/<subject>")
def income_approach(subject):
	subject = ast.literal_eval(subject)
	return render_template('income_approach.html', subject=subject)

@app.route("/cost_approach/<subject>")
def cost_approach(subject):
	# subject = ast.literal_eval(subject)
	return render_template('cost_approach.html', subject=subject)

if __name__ == "__main__":
	app.debug = True
	app.run()