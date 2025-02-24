from sqlmodel import SQLModel, Field
from typing import Optional

class Person(SQLModel, table=True):
	__tablename__ = 'People'
	id: Optional[int] = Field(default = None, primary_key = True)
	lastname: str = Field(default = '(lastname)', min_length = 3, max_length = 50, nullable = False)
	firstname: str = Field(default = '(firstname)', min_length = 3, max_length = 50, nullable = False)
	age: int = Field(default = 18, nullable = False, gt = 0, lt = 111)