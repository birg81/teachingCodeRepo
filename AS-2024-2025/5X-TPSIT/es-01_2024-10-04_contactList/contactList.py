import os
# Phonebook
contactList = {
	'firstcontact':	'+393xxxxxxxxx'
}
# clear your screen
# KEEPING: for UNIX Like OS must change CLS to clear
def clear():
	os.system('CLS')
# print your contact list and order your contacts by name
def printList():
	clear()
	order_contacts = sorted(contactList.keys())
	if len(order_contacts) > 0:
		for contact in order_contacts:
			print(f'* "{contact}" > {contactList[contact]}')
	else:
		print('(empty list)')
# search contact name by partial string
def searchList():
	clear()
	name = input('Insert partial name: ').strip().lower()
	for contact in contactList:
		if name in contact:
			print(f'* "{contact}" > {contactList[contact]}')
# add new Contact
def addContact():
	clear()
	name = input('Insert contact name: ').strip().lower()
	if name not in contactList:
		contactList[name] = input('Insert mobile number: ').strip().lower()
		print(f'{name} has been successfully added to the list...')
	else:
		print(f'{name} is already in the list...')
# remove your contact
def removeContact():
	clear()
	name = input('Insert contact name: ').strip().lower()
	if name in contactList:
		del contactList[name]
		print(f'{name} has been removed from the list successfully...')
	else:
		print(f'{name} not in the list...')
# modify mobile number
def modifyContact():
	clear()
	name = input('Insert contact name: ').strip().lower()
	if name in contactList:
		contactList[name] = input('Insert mobile number: ').strip().lower()
		print(f"{name}'s contact number has been updated successfully...")
	else:
		print(f'{name} not in the list...')
# rename your contact name
def renameContact():
	clear()
	name = input('Insert contact name: ').strip().lower()
	if name in contactList:
		newname = name
		while newname == name:
			newname = input(f'Insert new contact name (must be different to "{name}"): ').strip().lower()
		contactList[newname] = contactList[name]
		del contactList[name]
		print(f"{name}'s information has been updated successfully...")
	else:
		print(f'{name} not in the list...')