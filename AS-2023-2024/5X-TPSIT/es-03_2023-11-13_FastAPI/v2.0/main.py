import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
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

@webapp.get('/', response_class = HTMLResponse)
async def root(req:Request):
	return templates.TemplateResponse(
		'root.html', {
			'request': req,
			'author': 'birg81'
		}
	)

@webapp.get('/drawTab', response_class = HTMLResponse)
async def drawTab(req:Request, cols:int = 5, rows:int = 3):
	return templates.TemplateResponse(
		'drawTable.html', {
			'request': req,
			'cols': cols,
			'rows': rows
		}
	)

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)