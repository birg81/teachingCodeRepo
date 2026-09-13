import uvicorn
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

itemsList = []

def home(req: Request):
	itemsList.sort()
	return templates.TemplateResponse(
		# 'root.advance.html',
		'root.html',
		{
			'request': req,
			'title': 'ShoppingList',
			'itemsList': enumerate(itemsList)
		}
	)

# URL example:	./
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return home(req)

# URL example:	./create?item=mele
@webapp.get('/create', response_class = HTMLResponse)
async def create(req: Request):
	if 'item' in req.query_params and req.query_params['item'].strip() and req.query_params['item'].strip().lower() not in itemsList:
		itemsList.append(req.query_params['item'].strip().lower())
	return home(req)

# URL example:	./delete?id=5
@webapp.get('/delete', response_class = HTMLResponse)
async def delete(req: Request):
	if 'id' in req.query_params and req.query_params['id'].strip() and 0<= int(req.query_params['id'].strip()) < len(itemsList):
		itemsList.pop(int(req.query_params['id'].strip()))
	return home(req)

# URL example:	./update?id=5&item=mele
@webapp.get('/update', response_class = HTMLResponse)
async def update(req: Request):
	if 'item' in req.query_params and req.query_params['item'].strip() and req.query_params['item'].strip().lower() not in itemsList and 'id' in req.query_params and req.query_params['id'].strip() and 0<= int(req.query_params['id'].strip()) < len(itemsList):
		itemsList[int(req.query_params['id'].strip())] = req.query_params['item'].strip().lower()
	return home(req)