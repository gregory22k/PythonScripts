#import sqlite database program
import contactbook

print("Hello, what would you like to do?")

#User enters what to do next
print("""
Press 1 to insert one record: 
Press 2 to insert multiple records:
Press 3 to delete one record:
Press 4 to look up from a certain email: 
Press 5 to show all the records:
Press X to exit the application:
	""")
answer = input()

#Exit the program
if answer.lower() == 'x':
	exit()

#User adds one record
elif answer == '1':
	first_name = input("Enter the first name: ")
	last_name = input("Enter the last name: ")
	email = input("Enter the email: ")
	phone = input("Enter the phone: ")
	contactbook.add_one(first_name, last_name,email,phone)

#User adds multiple records
elif answer == '2':
	num_of = input("How many records do you want to add? ")
	contact_list = []
	for i in range(int(num_of)):
		cntct_first = input("Enter the first name of the contact: ")
		cntct_last = input("Enter the last name of the contact: ")
		cntct_email = input("Enter the email of the contact: ")
		cntct_number = input("Enter the phone number of the contact: ")
		cntct_tup=(cntct_first,cntct_last,cntct_email,cntct_number)
		contact_list.append(cntct_tup)
		print('\n')

	contactbook.add_many(contact_list)

#User deletes one record
elif answer == '3':
	id = input("Enter the row id you want to delete: ")
	contactbook.delete_one(id)

#User searches for a contact through email
elif answer == '4':
	email = input("Enter the email of the contact you are looking for: ")
	contactbook.lookup(email)

#Prints all records
elif answer == '5':
	contactbook.show_all()

#Invalid answer, user has to enter a valid one
else:
	print("Please enter a valid answer: ")