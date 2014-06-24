from helper import *
from constants import *
from sanitize import *

def filter_data(source, impr_sqft, age, dlrs_sqft):
	#Remove irrelevant comps from comp pool
	#Removes based on size, impairment, and distance
	tol = .1
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
						#Not younger and more expensive
						if not ((abs(source[a][14]-age) > 15) and (source[a][14] * .85 > dlrs_sqft)):
							result.append(source[a])

	result = sorted(result,key=lambda l:l[13], reverse=False)
	return result

def select_comps(source, dlrs_sqft):
	comps = []
	for comp in source:
		if comp[13] < dlrs_sqft:
			comps.append(comp)
		if len(comps) == 5:
			return comps
	return comps

def find_comps(address, impr_sqft, price, age, use, level, condition):
	#Get the coordinates of subject
	coor = get_coor(address)
	#Sanitize data
	cleaned_data = sanitize_combine(coor[0], coor[1])
	#Find usable age
	age = useful_life(use, level, condition, age)
	#Find the $/sqft
	dlrs_sqft = price / impr_sqft
	#Remove bad comps
	filtered_data = filter_data(cleaned_data, impr_sqft, age, dlrs_sqft)
	#Grab the top 5 best of the good comps
	comp_ids = select_comps(filtered_data, dlrs_sqft)
	return comp_ids

def save_subject(source):
	# with open('../comp_data/subject.csv','wb') as result:
	with open('../PropCalc/comp_data/subject.csv','wb') as result:
		resultfile = csv.writer(result, delimiter=',')
		resultfile.writerow(source)
	return

	# source_propertyline = csv_to_list('../PropCalc/comp_data/propertyline_data.csv')

def print_comps(comp_ids):
	for comp in comp_ids:
		print comp

# coor = get_coor('1502 Champion Dr Carrollton, TX 75006')
# print sanitize_combine(coor[0], coor[1])
# print_comps(find_comps('1502 Champion Dr Carrollton, TX 75006', 120644, 3867930, 28, 'Light Manufacturing', 'C', 'Average',))











