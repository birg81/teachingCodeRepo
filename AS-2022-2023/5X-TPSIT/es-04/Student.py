"""
Python, like C ++, is a multiple inheritance language. To inherit a class, simply open the brackets and write the name of the superclass.
Example
class A (B):
it means that A inherits from B
"""

from Person import Person

class Student(Person):
	'Student template class'

	def __init__(
		self,
		firstname = '', lastname = '', age = -1,
		school = ''
	):
		# super class
		super().__init__(firstname, lastname, age)
		# private method
		self.__school = 'ITI Renato Elia' if not school.strip() else school.strip()

# to string
	def __str__(self):
		return f"{super().__str__()}. I'm study at {self.__school}"

# getter / setter
	def get_school(self):
		return school

	def set_school(self, school):
		self.__school = school.strip() if school.strip() else self.__school