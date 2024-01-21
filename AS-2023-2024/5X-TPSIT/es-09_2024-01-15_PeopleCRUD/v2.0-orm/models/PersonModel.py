from db.database import Base
from sqlalchemy import Column, Integer, String

class PersonModel(Base):
	__tablename__ = 'People'
	id = Column(Integer, primary_key = True)
	firstname = Column(String(48), nullable = False)
	lastname = Column(String(48), nullable = False)
	age = Column(Integer, nullable = False)