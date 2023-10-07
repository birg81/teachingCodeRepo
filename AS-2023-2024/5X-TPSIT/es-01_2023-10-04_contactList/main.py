from contactList import *

clear()
if __name__ == '__main__':
	continueLoop = True
	while continueLoop:
		choice = int(input('''
*********** MENU **********
1. Show contact list
2. Search for contacts
3. Add a new contact
4. Delete contact
5. Edit contact's number
6. Edit contact
*. (screen refresh)\n
0. EXIT
***************************\n\n
(insert your choice) >_: '''
	))

		if choice == 0:
			continueLoop = False
		elif choice == 1:
			printList()
		elif choice == 2:
			searchList()
		elif choice == 3:
			addContact()
		elif choice == 4:
			removeContact()
		elif choice == 5:
			modifyContact()
		elif choice == 6:
			renameContact()
		else: # other choice make a screen refresh
			clear()

	print("\n\nThank you for using our software.\n")