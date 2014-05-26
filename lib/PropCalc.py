import math

def distance_on_unit_sphere(lat1, long1, lat2, long2):

	# Convert latitude and longitude to 
	# spherical coordinates in radians.
	degrees_to_radians = math.pi/180.0

	# phi = 90 - latitude
	phi1 = (90.0 - lat1)*degrees_to_radians
	phi2 = (90.0 - lat2)*degrees_to_radians

	# theta = longitude
	theta1 = long1*degrees_to_radians
	theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
	cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + math.cos(phi1)*math.cos(phi2))
	arc = math.acos(cos)

	# Remember to multiply arc by the radius of the earth 
	# in your favorite set of units to get length.
	return arc * 3960

import csv
def csv_to_list(file_path):
	datafile = open(file_path, 'r')
	datareader = csv.reader(datafile)
	data = []
	for row in datareader:
		data.append(row)
	return data

from datetime import date
def sanitize_raw_costar(source, lat1, long1):
	first = True
	result = []
	for a in range(len(source)):
		if first:
			first = False
		else:
			if source[a][126].find('(') == -1:
				result_row = [''] * 16

				#Account Number: 46
				result_row[0] = source[a][46]
				#Owner Name: 13
				result_row[1] = source[a][13]
				#Property Address: 126
				result_row[2] = source[a][126]
				#City: 127
				result_row[3] = source[a][127]
				#State: 130
				result_row[4] = source[a][130]
				#County: 128
				result_row[5] = source[a][128]
				#Impr Sqft: 7
				result_row[6] = source[a][7]
				#Land Sqft: 65
				result_row[7] = source[a][65]
				#Built: 193
				result_row[8] = source[a][193]
				#Note 1: 9
				result_row[9] = source[a][9]
				#Note 2: 144
				result_row[10] = source[a][144]
				#Sales Price: 146
				result_row[11] = source[a][146]
				#Sale Date: 145
				result_row[12] = source[a][145]
				#$/Sqft 
				result_row[13] = float(result_row[11]) / float(result_row[6])
				#Age
				result_row[14] = date.today().year - int("0" + result_row[8])
				#Distance 
				#Latitude: 69
				#Longitude: 84
				result_row[15] = distance_on_unit_sphere(lat1, long1, float(source[a][69]), float(source[a][84]))

				result.append(result_row)
				
	return result

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

def filter_data(source, impr_sqft, age):
	result = []
	for a in range(len(source)):
		#Size at least 66% and at most 200%
		if (impr_sqft * .66) <= int(source[a][6]) <= (impr_sqft * 2):
			#Check Note 1 for impariment
			if not_impaired(source[a][9]):
				#Check Note 2 for impariment
				if not_impaired(source[a][10]):
					#At most 15 miles away
					if source[a][15] <= 10:
						result.append(source[a])
	result = sorted(result,key=lambda l:l[13], reverse=False)
	return result

def select_comps(source, impr_sqft, age, price):
	comps = []
	dlrs_sqft = price / impr_sqft
	for comp in source:
		if comp[13] < dlrs_sqft:
			comps.append(comp)
		if len(comps) == 5:
			return comps
	return comps

from pygeocoder import Geocoder
def get_coor(address):
	result = [''] * 2
	coor = Geocoder.geocode(address)
	result[0] = coor.latitude
	result[1] = coor.longitude
	return result

def PropCalc(file_path, address impr_sqft, age, price):
	raw = csv_to_list(file_path)
	coor = get_coor(address)
	cleaned_data = sanitize_raw_costar(raw, coor[0], coor[1])
	filtered_data = filter_data(cleaned_data, impr_sqft, age)
	comp_ids = select_comps(filtered_data, impr_sqft, age, price)

	for comp in comp_ids:
		print comp

def main():
	# file_path = '/home/adam/Code/PropCalc/' + raw_input('Enter csv data file name: ')
	# lat1 = input('Enter lattitude: ')
	# long1 = input('Enter longitude: ')
	# age = input('Enter property age: ')
	# impr_sqft = input('Enter building square feet: ')
	# price = input('Enter sale price: ')

	# PropCalc(file_path, lat1, long1, impr_sqft, age, price)

	PropCalc('/home/adam/Code/PropCalc/test.csv','1502 Champion Dr Carrollton, TX 75006', 120644, 28, 3867930)

main()
















