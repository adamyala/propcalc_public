from helper import *

def not_impaired(source):
	constants = [
	'Partial Interest Transfer',
	'Sale Leaseback',
	'High Vacancy Property',
	'Purchase By Tenant',
	'Estate/Probate Sale',
	'Distress Sale',
	'REO Sale',
	'Bankruptcy Sale'
	]

	for trait in constants:
		if source.find(trait) != -1:
			return False
	return True

def useful_life(use, level, condition, age):
	result = ''
	constants = csv_to_list(main_dir + 'const_data/use_life.csv')
	for row in constants:
		if row[0] == use:
			if row[1] == level:
				if row[2] == condition:
					return float(row[3])
	return float(age)
