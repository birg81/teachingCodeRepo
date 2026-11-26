from uvicorn import run
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(
	title = 'Emoji Table',
	description = 'How show an emoji table with different approaches to parameter passing'
)
templates = Jinja2Templates(directory = 'templates')
'''
# 1. approach: Query Prameters -> Content-Type: text/html
GET	http://127.0.0.1:8000?rows=4&cols=3 -> HTML page
'''
@app.get('/', response_class = HTMLResponse)
async def html_by_queryParameters(req:Request, rows:int = 4, cols:int = 3):
	return templates.TemplateResponse(
		req,
		'emojiTab.html', {
			'rows': rows,
			'cols': cols
		}
	)
'''
# 2. approach: Path Prameters -> Content-Type: text/html
GET	http://127.0.0.1:8000/4/2 -> HTML page
'''
@app.get('/{rows}/{cols}', response_class = HTMLResponse)
async def html_by_pathParameters(req:Request, rows:int = 4, cols:int = 3):
	return templates.TemplateResponse(
		req,
		'emojiTab.html', {
			'rows': rows,
			'cols': cols
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
