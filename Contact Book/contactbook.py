import sqlite3

#print all contacts
def show_all():

	#connect to database
	conn = sqlite3.connect("contacts.db")
	#create cursor
	c = conn.cursor()

	#query the database
	c.execute("SELECT rowid, * FROM contacts")

	items = c.fetchall()

	for item in items:
		print(item)

	#commit our command
	conn.commit()
	#close our connection
	conn.close()

#Add one record in our database
def add_one(first, last, email, phone):
	conn = sqlite3.connect("contacts.db")
	c = conn.cursor()
	c.execute('INSERT INTO contacts VALUES (?,?,?,?)',(first,last,email,phone))
	conn.commit()
	conn.close()

def add_many(list):
	conn = sqlite3.connect("contacts.db")
	c = conn.cursor()
	c.executemany('INSERT INTO contacts VALUES (?,?,?,?)',list)
	conn.commit()
	conn.close()

#Delete one record from our database
def delete_one(id):
	conn = sqlite3.connect("contacts.db")
	c = conn.cursor()
	c.execute("DELETE FROM contacts WHERE rowid = (?)", id)
	conn.commit()
	conn.close()


#Lookup with Where

def lookup(email):
	conn = sqlite3.connect('contacts.db')
	c = conn.cursor()
	c.execute("SELECT * from contacts WHERE email = (?)", (email,))		
	items = c.fetchall()

	for item in items:
		print(item)

	conn.commit()
	conn.close()


## Create a lookup for every category
#	if id_input == '2':
#		c.execute("SELECT * from contacts WHERE detail = (?)", (last,))
#		items = c.fetchall()
#
#		for item in items:
#			print(item)
#
#		conn.commit()
#		conn.close()
#	if id_input == '3':
#		c.execute("SELECT * from contacts WHERE detail = (?) = (?)", (email,))
#		items = c.fetchall()
#
#		for item in items:
#			print(item)
#
#		conn.commit()
#		conn.close()
#	if id_input == '4':
#		c.execute("SELECT * from contacts WHERE detail = (?)", (phone,))
#		items = c.fetchall()
#		for item in items:
#
#			print(item)
#
#		conn.commit()
#		conn.close()