import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

webapp = FastAPI()

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

@webapp.get('/operazione', response_class = HTMLResponse)
async def root(req: Request):
	operazione = req.query_params['operazione']
	n1 = float(req.query_params['num1'])
	n2 = float(req.query_params['num2'])
	risultato = 'PARAMETRI ERRATI'
	if operazione == '+':
		risultato = f'{n1} + {n2} = {n1 + n2}'
	elif operazione == '-':
		risultato = f'{n1} - {n2} = {n1 - n2}'
	elif operazione == '/':
		risultato = f'{n1} ÷ {n2} = {n1 / n2}'
	elif operazione == '*':
		risultato = f'{n1} × {n2} = {n1 * n2}'
	return templates.TemplateResponse(
		'root.html',
		{
			'request': req,
			'risultato': risultato
		}
	)

@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html',
		{
			'request': req
		}
	)


if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 8000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)