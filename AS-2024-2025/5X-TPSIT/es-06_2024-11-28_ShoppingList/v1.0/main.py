import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

webapp = FastAPI(
	title = 'ShoppingList',
	decription = 'Web Example: Shopping list with Jinja Templating'
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

itemsList = []

# URL example:	./
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	itemsList.sort()		# sort your list
	return templates.TemplateResponse(
		'root.html', {
			'request': req,
			'itemsList': enumerate(itemsList)		# for send key and value
		}
	)

# URL example:	./create?item=mele
@webapp.get('/create')
async def create(item:str, req: Request):
	item = item.strip().lower()
	if item and item not in itemsList:
		itemsList.append(item)
		itemsList.sort()
	return RedirectResponse('/')

# URL example:	./update?id=5&item=mele
@webapp.get('/update')
async def update(id:int, item:str, req: Request):
	item = item.strip().lower()
	if 0 <= id < len(itemsList) and item and item not in itemsList:
		itemsList[id] = item
		itemsList.sort()
	return RedirectResponse('/')

# URL example:	./delete?id=5
@webapp.get('/delete')
async def delete(id:int, req: Request):
	if 0 <= id < len(itemsList):
		itemsList.pop(id)
	return RedirectResponse('/')

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)