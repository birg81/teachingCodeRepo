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

# start your main file
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		# 'root.advance.html',
		'root.html',
		{
			'request': req,
			'title': 'ShoppingList',
		}
	)

# [CREATE] :: POST Method - create (add) new item in your list and send a json message
# example (POST) ./api/apple -> append apple item in your itemsList
@webapp.post('/api/{item}')
async def create(item: str = ''):
	if item and item.strip() and item.strip().lower() not in itemsList:
		itemsList.append(item.strip().lower())
		return {
			'message': f'add "{itemsList[-1]}" to list!..',
			'success': True
		}
	return {
		'message': f'maybe "{item}" is already in your list..',
		'success': False
	}

# [READ] :: GET Method - read items from your list with json response
# example (GET) ./api/ -> sort and show all items from your itemsList
@webapp.get('/api')
async def read():
	itemsList.sort()
	return itemsList

# [UPDATE] :: PUT Method - modify (update) a specific item form index and response with json message
# example (PUT) ./api/1/apple -> change item at index 3 in apple
@webapp.put('/api/{id}/{item}')
async def update(id: int = -1, item: str = ''):
	if 0 <= id < len(itemsList) and item and item.strip() and item.strip().lower() not in itemsList:
		oldItem, itemsList[id] = itemsList[id], item.strip().lower()
		return {
			'message': f'update "{oldItem}", change to "{itemsList[id]}"..',
			'success': True
		}
	return {
		'message': f'maybe "{item}" is already in your list or maybe {id} is not a valid index..',
		'success': False
	}

# [DELETE] :: DELETE Method - Delete a specific item form index and response with json message
# example (DELETE) ./api/3 -> remove item at index 3 in your itemsList
@webapp.delete('/api/{id}')
async def delete(id: int = -1):
	if 0 <= id < len(itemsList):
		return {
			'message': f'{itemsList.pop(id)} was removed..',
			'success': True
		}
	return {
		'message': f'maybe {id} is not a valid index..',
		'success': False
	}