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

def csv_to_list(file_path):
	datafile = open(file_path)
	data = []
	for row in datafile:
		data.append(row.strip().split(','))
	return data

#Account Number 46
#Owner Name 13
#Property Address 126
#City 127
#State 130
#County 128
#Impr Sqft 7
#Land Sqft 65
#Built 193
#Note 1 9
#Note 2 144
#Sales Price 146
#Sale Date 145
#$/Sqft 
#Age
#Distance 

def sanitize_raw(source):
	first = True
	result = []
	print source[0]
	print source[0][126]
	# for a in range(len(source)):
		# if first:
		# 	first = False
		# else:
		# 	print source[a][126]
		# 	if not source[a][126].find('('):
		# 		result_row = [''] * 16
		# 		result_row[0] = source[a][46]
		# 		result.append(result_row)
	return result

def main(file_path):
	raw = csv_to_list(file_path)
	data = sanitize_raw(raw)

	#print data[0]

main('/home/adam/Code/PropCalc/test.csv')














