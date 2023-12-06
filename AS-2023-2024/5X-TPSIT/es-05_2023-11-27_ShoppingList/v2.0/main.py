import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

webapp = FastAPI(
	title = 'ShoppingList',
	decription = 'Web Example: Shopping list with ReST-API approach'
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

# start your main file
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html', {
			'request': req
		}
	)

# [CREATE] :: POST Method - create (add) new item in your list and send a json message
# example (POST) ./api/apple -> append apple item in your itemsList
@webapp.post('/api/{item}')
async def create(item: str = ''):
	item = item.strip().lower()
	if item and item not in itemsList:
		itemsList.append(item)
		itemsList.sort()
		return {
			'message': f'add {item.upper()} to list!..',
			'success': True
		}
	return {
		'message': f'maybe {item.upper()} is already in your list..',
		'success': False
	}

# [READ] :: GET Method - read items from your list with json response
# example (GET) ./api/ -> sort and show all items from your itemsList
@webapp.get('/api')
async def read():
	return itemsList

# [UPDATE] :: PUT Method - modify (update) a specific item form index and response with json message
# example (PUT) ./api/1/apple -> change item at index 3 in apple
@webapp.put('/api/{id}/{item}')
async def update(id: int = -1, item: str = ''):
	item = item.strip().lower()
	if 0 <= id < len(itemsList) and item and item not in itemsList:
		oldItem, itemsList[id] = itemsList[id], item
		itemsList.sort()
		return {
			'message': f'update {oldItem.upper()}, change to {item.upper()}..',
			'success': True
		}
	return {
		'message': f'maybe {item.upper()} is already in your list or maybe {id} is not a valid index..',
		'success': False
	}

# [DELETE] :: DELETE Method - Delete a specific item form index and response with json message
# example (DELETE) ./api/3 -> remove item at index 3 in your itemsList
@webapp.delete('/api/{id}')
async def delete(id: int = -1):
	if 0 <= id < len(itemsList):
		return {
			'message': f'{itemsList.pop(id).upper()} was removed..',
			'success': True
		}
	return {
		'message': f'maybe {id} is not a valid index..',
		'success': False
	}

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)