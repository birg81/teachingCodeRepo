import uvicorn
from model import characters
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

webapp = FastAPI(
	title = 'HTML Project',
	decription = 'Your 1st HTML & Jinja Templating Project!'
)

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

webapp.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)

@webapp.get('/', response_class = HTMLResponse)
async def index(req:Request):
	return templates.TemplateResponse(
		'characters.v1.html', {
			'request': req,
			'characters': characters
		}
	)

@webapp.get('/api/v2/characters.json')
async def charactersjson():
	return characters

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 8080,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)