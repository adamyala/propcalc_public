import sqlite3

with sqlite3.connect("propcalc.db") as connection:
	c = connection.cursor()

	c.execute("CREATE TABLE subjects(owner TEXT, pin TEXT, street TEXT, city TEXT, state TEXT, zipcode INT, impr_sqft INT, land_sqft INT, price INT, age INT, use TEXT, level TEXT, condition TEXT)")
	c.execute('INSERT INTO subjects VALUES("Ryerson", "140171000302R0000", "1502 Champion Dr", "Carrollton", "TX", 75006, 120644, 279132, 3867930, 28, "Light Manufacturing", "C", "Average")')
	c.execute('INSERT INTO subjects VALUES("Ryerson", "00000700134000000", "4606 Singleton Blvd", "Dallas", "TX", 75212, 141251, 412600, 2923900, 54, "Light Manufacturing", "S", "Low Cost")')


	print 'ran with no errors'