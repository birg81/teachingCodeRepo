import uuid
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

templates = Jinja2Templates(
	directory = 'templates'
)

app.add_middleware(
	SessionMiddleware,
	secret_key = 'your_secret_key'
)

@app.get('/', response_class = HTMLResponse)
async def root(req: Request):
	req.session['counter'] = req.session.get('counter', 0) + 1
	req.session['id'] = req.session.get('id', f'{uuid.uuid4().hex}')
	return templates.TemplateResponse(
		'root.html', {
			'request': req
		}
	)

@app.get('/clear-session')
async def clear_session(req: Request):
	req.session.clear()
	return RedirectResponse('/')

if __name__ == '__main__':
	uvicorn.run(
		'main:app',
		http = 'httptools',
		host = '0.0.0.0',
		port = 80,
		reload = True
	)
