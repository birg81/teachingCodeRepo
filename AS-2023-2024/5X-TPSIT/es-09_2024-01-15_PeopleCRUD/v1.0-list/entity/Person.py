from pydantic import BaseModel

class Person(BaseModel):
	id: int
	firstname: str
	lastname: str
	age: int