import uvicorn
import mysql.connector
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

# start your main file
@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html',
		{
			'request': req,
			'title': 'Movies',
		}
	)
@webapp.get('/api/{title}')
async def search(title: str):
	con = mysql.connector.connect(
		host="localhost",
		port=3306,
		user="root",
		password="",
		database="sakila"
	) 
	cur = con.cursor()
	whereContr = f'''
WHERE title LIKE '%{title}%'
	'''.strip() if title and title.strip() else ''
	q = f'''
SELECT *
FROM Film
{whereContr}
ORDER BY
	title ASC;
	'''.strip()
	cur.execute(q)
	rs=cur.fetchall()
	
	cur.close()
	con.close()
	myJson = []
	for row in rs:
		myJson.append(
			{
				"film_id": int(row[0]),
				"title": row[1].lower(),
				"description": row[2].lower(),
				"length": int(row[9])
			}
		)
	return myJson

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 4445,
		http = 'httptools',
		reload = True
	)