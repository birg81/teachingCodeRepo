import uvicorn
# from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

webapp = FastAPI()

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
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html',
		{
			'request': req,
			'title': 'Pagina di prova',
			'M': 8
		}
	)
