from pydantic import BaseModel, Field, validator
from typing import Literal

class Person(BaseModel):
	id: int = Field(..., gt = 0, description="ID must be an integer greater than 0")
	firstname: str = Field(..., min_length = 3, description="Firstname must be a string with at least 3 characters")
	lastname: str = Field(..., min_length = 3, description="Lastname must be a string with at least 3 characters")
	gender: Literal['m', 'f'] = Field(..., description="Gender must be either 'm' (male) or 'f' (female)")

	@validator('gender')
	def check_gender(cls, value):
		if value not in ['m', 'f']:
			raise ValueError("Gender must be either 'm' or 'f'")
		return value