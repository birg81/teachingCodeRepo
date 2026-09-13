"""
This file contains the Person class.
There are some advanced aspects in this version.
Although python OOP does not require getters and setters, it is useful to use them to better manage data.
There are no private / public attributes in Python.
There is a naming convention:
__ for private method
_ for protected method
nothing for public method
without 'self' for static attributes
"""

class Person:
	# you can read this line if you wrote p.__doc__ with p is a Person var kind
	'Person Template class'

	__countPeople = 0	# static private method

	# this is a constructor. In python way is called initializator
	def __init__(
		self,			# OBLIGATORY! implicit reference to your object
		# Default Parameter
		firstname = '', lastname = '', age = -1
	):
		# instance protected variables are set only if the method parameter values ​​are not inconsistent or set on default values
		self._firstname = 'Biagio' if not firstname.strip() else firstname.strip()
		self._lastname = 'Greco' if not lastname.strip() else lastname.strip()
		self._age = 17 if age < 0 else age
		# this variable counts the number of objects that have been instantiated
		Person.__countPeople += 1

	# cast to string - toString() method
	def __str__(self):
		return f"I'm {self.fullname()}, I'm {self._age}"

	# Getters methods
	def size(self):		#return instances objects numbers
		return Person.__countPeople

	def get_firstname(self):
		return self._firstname

	def get_lastname(self):
		return self._lastname

	def get_age(self):
		return self._age

	# return full name
	def fullname(self):
		return f'{self._firstname} {self._lastname}'

	# Setters methods
	def set_firstname(self, firstname):
		self._firstname = firstname.strip() if firstname.strip() else self._firstname

	def set_lastname(self, lastname):
		self._lastname = lastname.strip() if lastname.strip() else self._firstname

	def set_age(self, age):
		self._age = age if age >= 0 else self._age