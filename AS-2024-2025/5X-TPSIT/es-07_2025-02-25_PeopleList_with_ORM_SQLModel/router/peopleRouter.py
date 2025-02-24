from sqlmodel import Session
from model.Person import Person
from db.connection import getConnection
from fastapi import APIRouter, Depends, HTTPException

# Crea un router per gestire le rotte CRUD
router = APIRouter(
	tags = ['Person'],
	prefix = '/api/person'
)

# Route per ottenere tutte le persone
@router.get('/')
async def getAllPeople(db: Session = Depends(getConnection)):
	people = db.query(Person).all()
	if not people:
		raise HTTPException(
			status_code = 404,
			detail = 'No people found'
		)
	return people

# Route di esempio per ottenere un utente
@router.get('/{id}')
async def getPerson(id: int, db: Session = Depends(getConnection)):
	p = db.query(Person).filter(Person.id == id).first()
	if not p:
		raise HTTPException(
			status_code = 404,
			detail = 'User not found'
		)
	return p

# Route per creare un nuovo utente
@router.post('/')
async def createPerson(p: Person, db: Session = Depends(getConnection)):
	db.add(p)
	db.commit()
	db.refresh(p)
	return p

# Route per aggiornare una persona
@router.put('/{id}')
async def updatePerson(id: int, p: Person, db: Session = Depends(getConnection)):
	currentPerson = db.query(Person).filter(Person.id == id).first()
	if not currentPerson:
		raise HTTPException(
			status_code = 404,
			detail = 'User not found'
		)

	# Aggiorna i campi della persona
	currentPerson.firstname = p.firstname
	currentPerson.lastname = p.lastname
	currentPerson.age = p.age

	db.commit()
	db.refresh(currentPerson)
	return currentPerson

# Route per rimuovere una persona
@router.delete('/{id}')
async def deletePerson(id: int, db: Session = Depends(getConnection)):
	p = db.query(Person).filter(Person.id == id).first()
	if not p:
		raise HTTPException(
			status_code = 404,
			detail = 'User not found'
		)
	db.delete(p)
	db.commit()
	return {
		'detail': 'Person deleted successfully'
	}