from sqlalchemy import exc
from entity.Person import Person
from db.database import SessionLocal
from models.PersonModel import PersonModel
from fastapi import APIRouter, HTTPException

router = APIRouter(
	tags = ['Person'],
	prefix = '/api/person'
)

session = SessionLocal()

@router.post('/')
async def createPerson(person: Person):
	session.add(
		PersonModel(
			id = person.id,
			firstname = person.firstname.strip(),
			lastname = person.lastname.strip(),
			age = person.age
		)
	)
	try:
		session.commit()
	except exc.SQLAlchemyError:
		session.rollback()
		raise HTTPException(detail = 'Unable to add new Person! Maybe same ID already exists!', status_code = 404)
	return 'Success! A new person has been added to the list!'

@router.get('/')
async def getPeople():
	return session.query(PersonModel).all()

@router.get('/{id}')
async def getPerson(id: int):
	p = session.query(PersonModel).filter(PersonModel.id == id).first()
	if p:
		return p
	raise HTTPException(detail = f'ID Person {id} not found!..', status_code = 404)

@router.put('/{id}')
async def modifyPerson(id: int, person: Person):
	try:
		session.query(PersonModel).filter(PersonModel.id == id).update({
			'firstname': person.firstname.strip(),
			'lastname': person.lastname.strip(),
			'age': person.age
		})
		session.commit()
	except exc.SQLAlchemyError:
		session.rollback()
		raise HTTPException(detail = f'Error! Unable remove Person id {id}', status_code = 404)
	return f'Person with ID {id} updated successfully'

@router.delete('/{id}')
async def removePerson(id: int):
	try:
		p = session.query(PersonModel).filter(PersonModel.id == id).delete()
		session.commit()
		if p:
			return f'Success! Correct remove Person ID {id}!'
		else:
			session.rollback()
			raise HTTPException(detail = f'Error! Unable remove Person id {id}', status_code = 404)
	except exc.SQLAlchemyError:
		session.rollback()
		raise HTTPException(detail = f'Error! Unable remove Person id {id}', status_code = 404)