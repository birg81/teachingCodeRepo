from json import load, dump, JSONDecodeError

def loadSoccers(fname:str) -> list:
	try:
		with open(fname, 'r', encoding = 'utf-8') as f:
			return load(f)
	except (FileNotFoundError, JSONDecodeError):
		return []

def saveSoccers(fname:str, sList:list):
	with open(fname, 'w', encoding = 'utf-8', newline = '\n') as f:
		dump(sList, f, indent = '\t', ensure_ascii = False)

def newInputSoccer() -> dict:
	soccer:dict = {}
	soccer['fullname'] = input('Insert name: ').strip()
	soccer['n'] = int(input('Insert jersey number: '))
	soccer['position'] = input(
'''
(F)orward
(M)idfielder
(D)efender
(G)oalkeeper

insert position: '''
	).strip()
	soccer['team'] = input('Insert Team: ').strip()
	return soccer

def addNewSoccer(sList:list, soccer:dict) -> bool:
	if soccer in sList:
		return False
	sList.append(soccer)
	return True

def printSoccers(sList: list):
	if not sList:
		print("(Empty List)")
		return

	print("#", *sList[0].keys(), sep="\t")
	print("-" * 40)

	for i, s in enumerate(sList):
		print(i, *s.values(), sep="\t")

def findSoccersByName(sList: list, name: str) -> list:
	name = "".join(name.lower().split())
	return [
		s for s in sList if name in "".join(s["fullname"].lower().split())
	]

def updateSoccer(sList:list, idx:int, soccer:dict) -> bool:
	if not 0 <= idx < len(sList) or any(soccer == s for i, s in enumerate(sList) if i != idx):
		return False
	sList[idx] = soccer
	return True

def delSoccer(sList:list, idx:int) -> bool:
	if not 0 <= idx < len(sList):
		return False
	del sList[idx]
	return True
