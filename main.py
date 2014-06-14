from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def start():
	return render_template('index.html')

from lib.prop_calc import *
@app.route("/main/", methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		file_path = '/home/adam/Code/PropCalc/comp_data/costar_data.csv'
		owner = request.form['owner']
		street = request.form['street']
		city = request.form['city']
		state = request.form['state']
		zipcode = request.form['zipcode']
		address = street + ' ' + city + ', ' + state + ' ' + zipcode
		impr_sqft = request.form['impr_sqft']
		land_sqft = request.form['land_sqft']
		price = request.form['price']
		dlrs_sqft = round(float(price) / float(impr_sqft),2)
		age = request.form['age']
		built = 2014 - int(age)
		use = request.form['use']
		level = request.form['level']
		condition = request.form['condition']
		comps = prop_calc(file_path, address, float(impr_sqft), float(price), float(age), use, level, condition)
	return render_template('results.html', **locals())

if __name__ == "__main__":
	app.debug = True
	app.run()