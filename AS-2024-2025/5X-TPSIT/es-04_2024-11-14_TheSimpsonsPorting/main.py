import json
import uvicorn
from typing import List
from Person import Person
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
	title = 'HTML Project',
	description = 'Your 1st HTML & Jinja Templating Project!'
)

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

app.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)

characters: List[Person] = [Person(**character) for character in json.loads(open('characters.json').read())]

@app.get('/', response_class = HTMLResponse)
async def index(req:Request):
	return templates.TemplateResponse(
		'characters.v1.html', {
			'request': req,
			'characters': characters
		}
	)

@app.get('/api/v2/characters.json')
async def charactersjson():
	return characters

if __name__ == '__main__':
	uvicorn.run(
		'main:app',
		host = '0.0.0.0',
		port = 80,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)