class Person:
	def __init__(self, firstname:str = 'Ciro', lastname:str = 'De Rosa', age:int = 17, isMale:bool = True):
		self._firstname: str = 'Ciro'
		self._lastname: str = 'De Rosa'
		self._age: int = 17
		self._isMale: bool = True

		self.firstname = firstname
		self.lastname = lastname
		self.age = age
		self.isMale = isMale

	@property
	def firstname(self) -> str:
		return self._firstname

	@firstname.setter
	def firstname(self, value:str) -> None:
		if isinstance(value, str):
			cleaned = value.strip()
			if len(cleaned) > 2:
				self._firstname = cleaned

	@property
	def lastname(self) -> str:
		return self._lastname

	@lastname.setter
	def lastname(self, value:str) -> None:
		if isinstance(value, str):
			cleaned = value.strip()
			if len(cleaned) > 2:
				self._lastname = cleaned

	@property
	def age(self) -> int:
		return self._age

	@age.setter
	def age(self, value:int) -> None:
		if isinstance(value, int) and not isinstance(value, bool) and value > 0:
			self._age = value

	@property
	def isMale(self) -> bool:
		return self._isMale

	@isMale.setter
	def isMale(self, value:bool) -> None:
		if isinstance(value, bool):
			self._isMale = value

	def __str__(self) -> str:
		return f"{self._firstname} {self._lastname} ({'♂' if self._isMale else '♀'}), age: {self._age}"

class Student(Person):
	def __init__(self, firstname:str = 'Paola', lastname:str = 'Cuomo', age:int = 15, isMale:bool = False, classroom:str = '4X'):
		super().__init__(firstname, lastname, age, isMale)
		self._classroom: str = '4X'
		self.classroom = classroom

	@property
	def classroom(self) -> str:
		return self._classroom

	@classroom.setter
	def classroom(self, value:str) -> None:
		if isinstance(value, str):
			cleaned = value.strip()
			if len(cleaned) > 0:
				self._classroom = cleaned

	def __str__(self) -> str:
		return f'[Student] {super().__str__()}, classroom: {self._classroom}'

class Teacher(Person):
	def __init__(self, firstname:str = 'Anna', lastname:str = 'Scapece', age:int = 32, isMale:bool = False, subject:str = 'PC Science'):
		super().__init__(firstname, lastname, age, isMale)
		self._subject: str = 'PC Science'
		self.subject = subject

	@property
	def subject(self) -> str:
		return self._subject

	@subject.setter
	def subject(self, value:str) -> None:
		if isinstance(value, str):
			cleaned = value.strip()
			if len(cleaned) > 0:
				self._subject = cleaned

	def __str__(self) -> str:
		return f'[Teacher] {super().__str__()}, subject: {self._subject}'
