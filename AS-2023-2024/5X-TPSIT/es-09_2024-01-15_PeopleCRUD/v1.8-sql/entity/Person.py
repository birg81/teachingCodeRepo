from pydantic import BaseModel, Field
from pydantic.types import PositiveInt

class Person(BaseModel):
	id: PositiveInt
	firstname: str = Field(min_length = 2, max_length = 48, default = "(firstname)")
	lastname: str = Field(min_length = 2, max_length = 48, default = "(lastname)")
	age: PositiveInt