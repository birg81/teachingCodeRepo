import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

webapp = FastAPI(
	title = 'Auth e JWT',
	decription = 'Web Example: Auth e JWT su MySQL DBMS'
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

@webapp.get('/', response_class = HTMLResponse, tags = ['HomePage'])
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html', {
			'request': req,
			'author': 'birg81',
		}
	)

import time
import jwt
from decouple import config


SECRET = b'f9c194151872cdf2e88831377e40d3d5bdc91773dd1c640b'
ALGORITHM = 'HS256'

def signJWT(id: int, username: str):
	payload = {
		'id': id,
		'username': username,
		'expires': time.time() + 600
	}
	token = jwt.encode(payload, SECRET, algorithm = ALGORITHM)
	print(token)
	return token

def decodeJWT(token: str):
	try:
		payload = jwt.decode(token, SECRET, algorithms = [ALGORITHM])
		return payload if time.time() <= payload['expires'] else None
	except:
		return {}

@webapp.get('/api/jwt', tags = ['JWT'])
async def prova():
	return decodeJWT(signJWT(35, 'birg81'))

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		use_colors = False,
		http = 'httptools',
		reload = True
	)