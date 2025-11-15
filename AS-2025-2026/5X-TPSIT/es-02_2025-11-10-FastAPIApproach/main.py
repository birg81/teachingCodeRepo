import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

class Person(BaseModel):
	firstname: str = Field(default='Turanga')
	lastname: str = Field(default='Leela')

app = FastAPI(
	title = 'My First App',
	description = 'Different approaches to parameter passing'
)

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

@app.get('/', response_class = HTMLResponse)
async def greeting0(req:Request):
	return templates.TemplateResponse(
		'greeting.html', {
			'request': req,
			'firstname': 'Hubert J.',
			'lastname': 'Farnsworth'
		}
	)

# http://localhost:8000/api/approach1/?firstname=Bart&lastname=Simpson
@app.get('/approach1', response_class = HTMLResponse)
async def greeting1(firstname: str, lastname: str, req:Request):
	return templates.TemplateResponse(
		'greeting.html', {
			'request': req,
			'firstname': firstname,
			'lastname': lastname
		}
	)

# http://localhost:8000/api/approach2/Bart/Simpson
@app.get('/approach2/{firstname}/{lastname}', response_class = HTMLResponse)
async def greeting2(firstname: str, lastname: str, req:Request):
	return templates.TemplateResponse(
		'greeting.html', {
			'request': req,
			'firstname': firstname,
			'lastname': lastname
		}
	)

# http://localhost:8000/api/approach3/ + JSON {'firstname': 'Bart', 'lastname': 'Simpson'}
@app.post('/approach3/', response_class = HTMLResponse)
async def greeting3(p: Person, req: Request):
	return templates.TemplateResponse(
		'greeting.html', {
			'request': req,
			'firstname': p.firstname if p != None else '(no firstname)',
			'lastname': p.lastname if p != None else '(no lastname)'
		}
	)

if __name__ == '__main__':
	uvicorn.run(
		'main:app',
		http = 'httptools',
		host = '0.0.0.0',
		port = 8000,
		reload = True
	)
