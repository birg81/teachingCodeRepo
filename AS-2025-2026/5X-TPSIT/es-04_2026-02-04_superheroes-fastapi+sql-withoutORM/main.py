import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector as db

app = FastAPI(
	title = 'Super Heroes List',
	decription = 'SQL without ORM: Jinja Templating vs json data responsing'
)

templates = Jinja2Templates (
	directory = 'templates',
	autoescape = False,
	auto_reload = True
)

app.mount(
	'/static',
	app = StaticFiles(directory = 'static'),
	name = 'static'
)

# for db connectiong, return connection object
def get_db():
	con = db.connect(
		host = 'localhost',
		port = 3306,
		user = 'root',
		password = '',
		database = 'SuperHeroes'
	)
	try:
		yield con
	finally:
		con.close()

# resolve query for get all heroes
def get_heores(con):
	cur = con.cursor(dictionary = True)
	cur.execute("""
	SELECT
		id,
		firstname, lastname,
		isHuman,
		supername
	FROM
		HeroesList
	ORDER BY
		supername ASC,
		lastname ASC,
		firstname ASC;
	""")
	rs = cur.fetchall()
	cur.close()
	return rs

# pure html + json data responsing with js
@app.get('/', response_class = HTMLResponse)
async def index(req: Request):
	return templates.TemplateResponse(
		'index.html', {
			'request': req
		}
	)

# pure json data
@app.get('/api/superheroes')
async def superheroesjson(con = Depends(get_db)):
	return get_heores(con)

# Jinja Templating
@app.get('/homeTab', response_class = HTMLResponse)
async def homeTab(req: Request, con = Depends(get_db)):
	return templates.TemplateResponse(
		'homeTab.html', {
			'request': req,
			'heroes': get_heores(con)
		}
	)

if __name__ == '__main__':
	uvicorn.run(
		'main:app',
		http = 'httptools',
		host = '0.0.0.0',
		port = 3000,
		reload = True
	)