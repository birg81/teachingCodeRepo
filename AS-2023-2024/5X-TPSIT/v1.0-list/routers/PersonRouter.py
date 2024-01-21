from entity.Person import Person
from fastapi import APIRouter, HTTPException

router = APIRouter(
	tags = ['Person'],
	prefix = '/api/person'
)

people = [
	Person(id = 1,	firstname = 'Gennaro',		lastname = 'Esposito',		age = 30),
	Person(id = 2,	firstname = 'Antonio',		lastname = 'Russo',			age = 25),
	Person(id = 3,	firstname = 'Maria',		lastname = 'Ferraro',		age = 28),
	Person(id = 4,	firstname = 'Carmela',		lastname = 'De Luca',		age = 45),
	Person(id = 5,	firstname = 'Pasquale',		lastname = 'Coppola',		age = 17),
	Person(id = 6,	firstname = 'Rosa',			lastname = 'Romano',		age = 22),
	Person(id = 7,	firstname = 'Salvatore',	lastname = 'Di Martino',	age = 33),
]

@router.post('/')
async def createPerson(person: Person):
	if person.id > 0 and len([p for p in people if p.id == person.id]) == 0:
		people.append(person)
		return 'Success! A new person has been added to the list!'
	raise HTTPException(detail = 'Unable to add new Person! Maybe same ID already exists!', status_code = 404)

@router.get('/')
async def getPeople():
	return people

@router.get('/{id}')
async def getPerson(id:int):
	pList = [p for p in people if p.id == id]
	if len(pList) > 0:
		return pList[0]
	raise HTTPException(detail = f'ID Person {id} not found!..', status_code = 404)

@router.put('/{id}')
async def modifyPerson(id: int, person: Person):
	if any(p.id == id for p in people) and person.id == id:
		people[:] = [p for p in people if p.id != id]
		people.append(person)
		return f'Person with ID {id} updated successfully'
	raise HTTPException(detail = f'Unable to update Person with ID {id}. Person not found', status_code = 404)

@router.delete('/{id}')
async def removePerson(id:int):
	if any(p.id == id for p in people):
		people[:] = [p for p in people if p.id != id]
		return f'Success! Correct remove Person ID {id}!'
	raise HTTPException (detail = f'Error! Unable remove Person id {id}', status_code = 404)