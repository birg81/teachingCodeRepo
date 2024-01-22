from entity.Person import Person
from fastapi import APIRouter, HTTPException
from db.database import selectFromTab, updateFromTab

router = APIRouter(
	tags = ['Person'],
	prefix = '/api/person'
)

@router.post('/')
async def createPerson(p: Person):
	if updateFromTab(f'INSERT INTO People(age, lastname, firstname) VALUES({p.age}, "{p.lastname}", "{p.firstname}");') > 0:
		raise HTTPException(detail = 'Unable to add new Person! Maybe same ID already exists!', status_code = 404)
	return 'Success! A new person has been added to the list!'

@router.get('/')
async def getPeople():
	return selectFromTab()

@router.get('/{id}')
async def getPerson(id: int):
	p = selectFromTab(f'id={id}')
	if len(p) > 0:
		return p[0]
	raise HTTPException(detail = f'ID Person {id} not found!..', status_code = 404)

@router.put('/{id}')
async def modifyPerson(id: int, p: Person):
	if updateFromTab(f"UPDATE People SET age={p.age}, lastname='{p.lastname}', firstname='{p.firstname}' WHERE id={id};") > 0:
		return f'Person with ID {id} updated successfully'
	raise HTTPException(detail = f'Error! Unable remove Person id {id}', status_code = 404)

@router.delete('/{id}')
async def removePerson(id: int):
	if updateFromTab(f'DELETE From People WHERE id={id};') > 0:
		return f'Success! Correct remove Person ID {id}!'
	raise HTTPException(detail = f'Error! Unable remove Person id {id}', status_code = 404)