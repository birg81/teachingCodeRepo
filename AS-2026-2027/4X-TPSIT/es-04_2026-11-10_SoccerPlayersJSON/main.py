from SoccersTools import (
	loadSoccers, saveSoccers,
	newInputSoccer,	addNewSoccer,
	printSoccers, findSoccersByName,
	updateSoccer,
	delSoccer
)

SOCCERS_FILE = './soccerplayers.json'

MENU = '''
1. Add new player
2. List players
3. Search players
4. Edit player
5. Remove player

0. EXIT

>_ '''

soccers = loadSoccers(SOCCERS_FILE)

choice:int = -1

while choice != 0:
	choice = int(input(MENU))
	match choice:
		case 0:
			saveSoccers(SOCCERS_FILE, soccers)
			break
		case 1:
			soccer = newInputSoccer()
			if addNewSoccer(soccers, soccer):
				saveSoccers(SOCCERS_FILE, soccers)
			else:
				print(f"ERROR: Player {soccer['fullname']} already exists")
		case 2:
			printSoccers(soccers)
		case 3:
			name = input("Insert name: ").strip()
			soccers_find = findSoccersByName(soccers, name)
			printSoccers(soccers_find)
		case 4:
			idx:int = int(input('Insert soccer index to modify: '))
			soccer = newInputSoccer()
			if updateSoccer(soccers, idx, soccer):
				saveSoccers(SOCCERS_FILE, soccers)
			else:
				print(f"ERROR: Player {soccer['fullname']} already exists")
		case 5:
			idx:int = int(input('Insert soccer index to remove: '))
			if delSoccer(soccers, idx):
				saveSoccers(SOCCERS_FILE, soccers)
			else:
				print(f'ERROR: No soccer player found with index {idx}')
		case _:
			print('Invalid choice. Please try again.')

print('Thanks for using our software...')
