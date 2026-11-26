from uvicorn import run
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI(
	title = 'ShoppingList'
)

templates = Jinja2Templates (
	directory = 'templates'
)

app.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)

itemsList = []

# URL example:	./
@app.get('/', response_class = HTMLResponse)
async def root(req: Request):
	itemsList.sort()		# sort your list
	return templates.TemplateResponse(
		req,
		'root.html', {
			'itemsList': enumerate(itemsList)		# for send key and value
		}
	)

# URL example:	./create?item=mele
@app.get('/create')
async def create(item:str, req: Request):
	item = item.strip().lower()
	if item and item not in itemsList:
		itemsList.append(item)
	return RedirectResponse('/')

# URL example:	./update?id=5&item=mele
@app.get('/update')
async def update(id:int, item:str, req: Request):
	item = item.strip().lower()
	if 0 <= id < len(itemsList) and item and item not in itemsList:
		itemsList[id] = item
	return RedirectResponse('/')

# URL example:	./delete?id=5
@app.get('/delete')
async def delete(id:int, req: Request):
	if 0 <= id < len(itemsList):
		itemsList.pop(id)
	return RedirectResponse('/')

if __name__ == '__main__':
	run(
		'main:app',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)
