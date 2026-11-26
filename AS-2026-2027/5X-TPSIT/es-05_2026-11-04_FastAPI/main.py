from uvicorn import run
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
	title = '1st FastAPI app',
	description = 'Different approaches to parameter passing'
)

templates = Jinja2Templates (
	directory = 'templates'
)

'''
# Default Approach: Content-Type: application/json
GET http://127.0.0.1:8000/ -> JSON Data
'''
@app.get('/')
async def json_greeting():
	return {
		'msg': 'Good news, everyone!'
	}

'''
# 1. approach: Query Prameters -> Content-Type: text/html
GET	http://127.0.0.1:8000/html/?fullname=Philip+J+Fry&times=7 -> HTML page
'''
@app.get('/html/', response_class = HTMLResponse)
async def html_greeting_by_QueryParameters(req:Request, fullname:str = 'everyone', times:int = 10):
	return templates.TemplateResponse(
		req,
		'greeting.html', {
			'fullname': fullname,
			'times': times
		}
	)

'''
# 2. approach: Path Prameters -> Content-Type: text/html
GET	http://127.0.0.1:8000/html/5/Philip+J+Fry -> HTML page
'''
@app.get('/html/{times}/{fullname}', response_class = HTMLResponse)
async def html_greeting_by_PathParameters(req:Request, fullname:str = 'everyone', times:int = 10):
	return templates.TemplateResponse(
		req,
		'greeting.html', {
			'fullname': fullname,
			'times': times
		}
	)

if __name__ == '__main__':
	run(
		'main:app',
		host = '0.0.0.0',
		port = 8000,
		http = 'httptools',
		reload = True
	)
