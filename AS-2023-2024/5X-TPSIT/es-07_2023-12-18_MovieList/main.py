import uvicorn
import mysql.connector as dbms
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

webapp = FastAPI(
	title = 'Movies List',
	decription = 'Web Example: Movies List by MySQL (Sakila[db])'
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

@webapp.get('/', response_class = HTMLResponse)
async def root(req: Request):
	return templates.TemplateResponse(
		'root.html', {
			'request': req,
		}
	)

@webapp.get('/api/{title}')
async def search(title: str = ''):
	FIELDS = ('film_id', 'title', 'description', 'length')
	whereContr = f'''
WHERE title LIKE '%{title}%'
	'''.strip() if title and title.strip() and title.strip() != '_' else ''
	q = f'''
SELECT
	{', '.join(FIELDS)}
FROM Film
{whereContr}
ORDER BY
	title ASC;
	'''.strip()
	con = dbms.connect(
		host = 'localhost', port = 3306,
		user = 'root', password = '',
		database = 'sakila'
	)
	cur = con.cursor()
	cur.execute(q)
	rs = cur.fetchall()
	cur.close()
	con.close()
	return [ {k: v for k, v in zip(FIELDS,row)} for row in rs ]

if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)