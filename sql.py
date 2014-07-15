import sqlite3

with sqlite3.connect("propcalc.db") as connection:
	c = connection.cursor()

	c.execute("CREATE TABLE subjects(owner TEXT, pin TEXT, street TEXT, city TEXT, state TEXT, zipcode INT, impr_sqft INT, land_sqft INT, price INT, age INT, use TEXT, level TEXT, condition TEXT, lat REAL, long REAL)")
	c.execute('INSERT INTO subjects VALUES("TexasProp1", "123456789012R0000", "123 Fake St", "Carrollton", "TX", 75006, 120644, 279132, 3867930, 28, "Light Manufacturing", "C", "Average", 32.932964, -96.91964)')
	c.execute('INSERT INTO subjects VALUES("TexasProp2", "12345678901200000", "567 Fake Blvd", "Dallas", "TX", 75212, 141251, 412600, 2923900, 54, "Light Manufacturing", "S", "Low Cost", 32.932964, -96.91964)')


	print 'ran with no errors'