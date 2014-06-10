from helper import *

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
				result_row[13] = round(float(result_row[11]) / float(result_row[6]),2)
				#Age
				result_row[14] = date.today().year - int("0" + result_row[8])
				#Distance 
				#Latitude: 69
				#Longitude: 84
				result_row[15] = round(distance_on_unit_sphere(lat1, long1, float(source[a][69]), float(source[a][84])),2)

				result.append(result_row)
				
	return result