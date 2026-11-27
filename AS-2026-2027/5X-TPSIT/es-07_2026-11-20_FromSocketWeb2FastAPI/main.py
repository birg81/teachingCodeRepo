from uvicorn import run
from random import choice
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from entities import quotes, soccerplayers, ingredients

app = FastAPI( title = 'Stream Socket web' )
templates = Jinja2Templates ( directory = 'templates' )
app.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)

@app.get('/api/soccerplayers')
async def players_list():
	return soccerplayers

@app.get('/api/ingredients')
async def potions():
	return ingredients

@app.get('/', response_class = HTMLResponse)
async def home(req:Request):
	return templates.TemplateResponse(
		req, 'home.html', {}
	)

@app.get('/html/quotes', response_class = HTMLResponse)
async def message_of_the_day(req:Request):
	return templates.TemplateResponse(
		req,
		'motd.html', {
			'quote': choice(quotes)
		}
	)

@app.get('/html/soccerplayers', response_class = HTMLResponse)
async def soccers(req:Request):
	return templates.TemplateResponse(
		req, 'soccersplayers.html', { }
	)

@app.get('/html/grimoire', response_class = HTMLResponse)
async def grimoire(req:Request):
	return templates.TemplateResponse(
		req, 'grimoire.html', { }
	)

if __name__ == '__main__':
	run(
		'main:app',
		http = 'httptools',
		host = '0.0.0.0',
		port = 3000,
		reload = True
	)
