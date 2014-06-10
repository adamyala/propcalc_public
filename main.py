from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def start():
	return render_template('index.html')

from PropCalc import *
@app.route("/main/", methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		file_path = '/home/adam/Code/PropCalc/comp_data/data.csv'
		street = request.form['street']
		city = request.form['city']
		state = request.form['state']
		zipcode = request.form['zip']
		address = street + ' ' + city + ', ' + state + ' ' + zipcode
		impr_sqft = request.form['impr_sqft']
		price = request.form['price']
		age = request.form['age']
		use = request.form['use']
		level = request.form['level']
		condition = request.form['condition']
		comps = PropCalc(file_path, address, float(impr_sqft), float(price), float(age), use, level, condition)
		# PropCalc('/home/adam/Code/PropCalc/comp_data/data.csv','1502 Champion Dr Carrollton, TX 75006', 120644, 3867930, 28, 'Light Manufacturing', 'C', 'Average')
		# PropCalc('/home/adam/Code/PropCalc/comp_data/data.csv','1502 Champion Dr Carrollton, TX 75006', 120644, 3867930, 28, 'Light Manufacturing', 'C', 'Average')
	return render_template('results.html', **locals())

if __name__ == "__main__":
	app.debug = True
	app.run()