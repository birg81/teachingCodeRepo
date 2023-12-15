import os
import random
import uvicorn
import aiofiles
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, File, UploadFile, Request

webapp = FastAPI(
	title = 'Upload File',
	decription = 'Upload binary file and save on server'
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

# start your main file
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html', {
			'request': req
		}
	)

@webapp.post('/upload')
async def uploadImg(imgFile: UploadFile = File(...)):
	imgFile.filename = f'{int(1_000_000*random.random()):06}.jpg'
	async with aiofiles.open(os.path.join("static", "img", imgFile.filename), "wb") as image:
		await image.write(await imgFile.read())

	return {"filename": imgFile.filename}

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)