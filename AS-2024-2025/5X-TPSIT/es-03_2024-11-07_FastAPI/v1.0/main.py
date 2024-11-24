import uvicorn
from fastapi import FastAPI

webapp = FastAPI(
	# This is an optional parameter. It is only shown in Swagger UI - change your WebApp's Name
	title = 'Ciao',
	# This is an optional parameter. It is only shown in Swagger UI
	description = 'This basic example describes how routes work and only returns json data'
)

# this function is used by all routes. It returns a dictionary
def greating(author: str = 'William', age: int = 18):
	return {
		'author': author,
		'age': age,
		'message': f'Hi!, I am {author} 👋🏼. I am {age} years old! 🎂'
	}

@webapp.get('/')
async def hello0():
	return greating('birg81', 42)

@webapp.get('/greating')
async def hello1(fullname: str = 'Catello', age: int = 19):
	return greating(fullname, age)

@webapp.get('/greating/{fullname}/{age}')
async def hello2(fullname: str = 'Mario', age: int = 21):
	return greating(fullname, age)

if __name__ == '__main__':
	uvicorn.run(
		# main: it is current filename, webapp: it is FastAPI object
		'main:webapp',
		# 0.0.0.0 you can replace with localhost or 127.0.0.1 or yout personal IP
		host = '0.0.0.0',
		# you can choice your favorite port number
		port = 3000,
		# use_colors = False,
		# You can display your webapp from every browser foreach device in your local network
		http = 'httptools',
		# autoreload server on source change
		reload = True
	)