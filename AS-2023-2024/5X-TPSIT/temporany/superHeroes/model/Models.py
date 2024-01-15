from pydantic import BaseModel

class SuperHero(BaseModel):
	id: int
	firstname: str
	lastname: str
	supername: str

class SuperPower(BaseModel):
	id: int
	power: str
	description: str