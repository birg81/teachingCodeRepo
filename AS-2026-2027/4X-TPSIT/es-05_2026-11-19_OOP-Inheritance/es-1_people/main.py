from model import (
	Person,
	Student, Teacher
)

if __name__ == '__main__':
	people:list[Person] = [
		Person(),
		Person('Anna', 'Di Maio', 27, False),
		Student(age = 16, firstname= 'Luca', classroom= '4G'),
		Student('Sofia', 'Rossi', 17, isMale=False, classroom= '5B'),
		Teacher(subject= 'Math', age= 45, lastname= 'Bianchi'),
		Teacher('El', 'Verdi', -5, False, subject= 'Physics'),
	]

	for p in people:
		print(p)

	print()
	print('-' * 15)
	print(f'\n{vars(people[0])}')
