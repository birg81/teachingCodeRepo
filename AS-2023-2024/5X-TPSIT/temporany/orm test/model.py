from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///./ormPythonDB.db')
	#'mysql://root:@localhost:3306/ormPythonDB')

Base = declarative_base()

class User(Base):
	__tablename__ = 'Users'
	id = Column(Integer, primary_key = True)
	email = Column(String(48))
	secret = Column(String(128))

Base.metadata.create_all(engine)