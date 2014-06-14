from helper import *
from datetime import date

def sanitize_combine(lat1, long1):
	source_costar = '../PropCalc/comp_data/costar_data.csv'
	result_costar = sanitize_raw_costar(source_costar, lat1, long1)
	source_loopnet = csv_to_list('../PropCalc/comp_data/loopnet_data.csv')
	result_loopnet = sanitize_raw_loopnet(source_loopnet, lat1, long1)

	result = source_costar.extend(source_loopnet)
	return result

def sanitize_raw_propertyshark(source, lat1, long1):
	first = True
	result = []
	for a in range(len(source)):
		if first:
			first = False
		else:
			if source[a][0] != 'Subscribe':
				result_row = [''] * 17
				#Account Number: 46
				result_row[0] = ''
				#Owner Name: 13
				result_row[1] = source[a][6]
				#Property Address: 126
				result_row[2] = source[a][0]
				#City: 127
				result_row[3] = ''
				#State: 130
				result_row[4] = ''
				#County: 128
				result_row[5] = ''
				#Impr Sqft: 7
				result_row[6] = ''
				#Land Sqft: 65
				result_row[7] = ''
				#Built: 193
				result_row[8] = ''
				#Note 1: 9
				result_row[9] = ''
				#Note 2: 144
				result_row[10] = ''
				#Sales Price: 146
				result_row[11] = ''
				#Sale Date: 145
				result_row[12] = ''
				#$/Sqft 
				result_row[13] = round(float(result_row[11]) / float(result_row[6]),2)
				#Age
				result_row[14] = date.today().year - int("0" + result_row[8])
				#Distance 
				#Latitude: 69
				#Longitude: 84
				result_row[15] = round(distance_on_unit_sphere(lat1, long1, float(source[a][69]), float(source[a][84])),2)
				#Source
				result_row[16] = 'PropertyShark'
				result.append(result_row)
	return result

def sanitize_raw_propertyline(source, lat1, long1):
	return result

def sanitize_raw_loopnet(source, lat1, long1):
	result= []
	result_row = ''
	# print source[0][0][:4]
	for a in range(len(source)):
		# print source[a][0][:4]
		if source[a][0][:4] == 'Sold':
			result_row = [''] * 17
			# Sale Date
			result_row[12] = source[a][0][5:findnth(source[a][0],' ',1)]
			# Sale Price
			result_row[11] = source[a][0][findnth(source[a][0],'$',0)+1:].replace(',','')
			#Property Address
			address = source[a+1][0].split(',')
			result_row[2] = address[0].strip()
			#City
			result_row[3] = address[1].strip()
			#State
			result_row[4] = address[2][:3].strip()
			#Note 1 and Note 2
			b = 0
			notes = ''
			while not source[a+b+2][0][0].isdigit():
				if notes == '':
					notes = source[a+b+2][0]
				else:
					notes = notes + ', ' + source[a+b+2][0]
				b += 1
			result_row[9+b] = notes
			#Impr Sqft
			result_row[6] = source[a+b+2][0][0:source[a+b+2][0].find('SF')].strip().replace(',','')
			b += 1
			#Built and Age
			print source[a+b+2][0][6:]
			if source[a+b+2][0][6:].isdigit():
				result_row[8] = source[a+b+2][0][6:]
				result_row[14] = date.today().year - int(result_row[8])
			#Distance
			address = result_row[2] + ' ' + result_row[3] + ', ' + result_row[4]
			# coor = get_coor(address)
			# result_row[15] = round(distance_on_unit_sphere(lat1, long1, float(coor[0]), float(coor[1])),2)
			#Source
			result_row[16] = 'LoopNet'
			result.append(result_row)


	for thingy in result:
		print thingy

print sanitize_raw_loopnet(csv_to_list('../comp_data/loopnet_data.csv'),32.932964,-96.91964)
# print get_coor('1502 Champion Dr Carrollton, TX 75006')

def sanitize_raw_costar(source, lat1, long1):
	first = True
	result = []
	for a in range(len(source)):
		if first:
			first = False
		else:
			if source[a][126].find('(') == -1:
				result_row = [''] * 17
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
				#Source
				result_row[16] = 'CoStar'

				result.append(result_row)	
	return result