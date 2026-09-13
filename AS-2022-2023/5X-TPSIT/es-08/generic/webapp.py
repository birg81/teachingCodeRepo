# file: webapp.py

# for use typing
from typing import Optional
#for sqlite3
import sqlite3
# server
import uvicorn
# FastAPI and Request params
from fastapi import FastAPI, Request
# for use HTML response
from fastapi.responses import HTMLResponse, PlainTextResponse
# for use templating
from fastapi.templating import Jinja2Templates

# conficure templates
templates = Jinja2Templates (
	directory='templates',	# template working directory
	autoescape=False,	# set False for insert html tag, True for plain text
	auto_reload=True
)

# create webapp obj
webapp = FastAPI()

# return a index html page
@webapp.get('/', response_class=HTMLResponse)
def index():
	w = [
		'lun', 'mar', 'mer',
		'gio', 'ven', 'sab',
		'dom'
	]
	return f'''
<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, shrink-to-fit=no, user-scalable=yes, initial-scale=1.0, maximum-scale=4.0, minimum-scale=0.5" />
<title>NAPOLI</title>
<link
	rel="icon"
	type="image/png"
	sizes="60x60"
	href="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/60/whatsapp/326/high-voltage_26a1.png"
/>
</head>
<body>
<h1>Napoli 1926</h1>
<ul>
<li><a href="./great/franco/pitone">&#x1f40d;</a></li>
<li><a href="./info/?param1=1st+param&param2=2nd+param">&#x2754;</a></li>
<li><a href="./welcome?title=blue+circle&rows=23&cols=54">&#x1f535;</a></li>
<li><a href="./sql/">&#x1f4c7;</a></li>
<li><a href="./tombola/">&#x1f385;</a></li>
{''.join(['<li>'+str(d)+'</li>' for d in w]).upper()}
{'<li>Forza Napoli &#x1f499;</li>'*3}
</ul>
</body>
</html>
	'''

# manage query string
@webapp.get('/great/{name}/{animal}')
async def great(name: str | None = '', animal: str | None = ''):
	if name is None or name.strip() == '':
		name = 'ARTURITO'
	if animal is None or animal.strip() == '':
		animal = 'DOG'
	return {
		"name": name,
		"animal": animal
	}

# return a info
@webapp.get('/info/')
async def test(req: Request):
	return {
		'client': req.client,
		'header': req.headers,
		'method': req.method,
		'url': req.url.path,
		'query_params': req.query_params,
		'path_params': req.path_params
	}

# for testing Jinja Templating
@webapp.get('/welcome', response_class=HTMLResponse)
async def welcome(req: Request):
	return templates.TemplateResponse(
		'drawCircle.html',
		{
			'request': req,
			'title':
				f'''{req.query_params['title'].strip()} &#x1f7e2;'''
				if
					'title' in req.query_params and
					req.query_params['title'] and
					req.query_params['title'].strip()
				else
					'No Tile &#x1f534;',
			'rows':
				int(req.query_params['rows'].strip())
				if
					'rows' in req.query_params and
					req.query_params['rows'] and
					req.query_params['rows'].strip()
				else
					4,
			'cols':
				int(req.query_params['cols'].strip())
				if
					'cols' in req.query_params and
					req.query_params['cols'] and
					req.query_params['cols'].strip()
				else
					3,
		}
	)

#
@webapp.get('/sql')
def loadSQLfil():
	# connect to local db
	con = sqlite3.connect('./personDB.db')
	sql = open('./PersonDB.sql', 'r').read().split(';')
	for q in sql:
		con.execute(f'''{q.strip()};''')
	con.commit()

	fields = ('id', 'lastname', 'firstname', 'gender', 'h', 'age')
	cur = con.execute(f'''SELECT {', '.join(fields)} FROM PersonList;''')
	json = []

	for row in cur:
		p = {}
		c = 0
		for v in row:
			p[fields[c]] = v
			c += 1
		json.append(p)
	con.close()

	return json

@webapp.get('/tombola', response_class=HTMLResponse)
async def tombola(req: Request):
	import random as r
	from datetime import datetime as dt

	lst = [i for i in range(1,91)]
	r.shuffle(lst)

	return templates.TemplateResponse(
		'tombola.html',
		{
			'request': req,
			'title': 'Tombola &#x1f385;',
			'numbers': lst[0:15],
			't': f'{dt.now().strftime("%H:%M:%S")}',
			'cardserie': int(10_000 * r.random())
		}
	)

'''
if __name__ == '__main__':
	uvicorn.run(
		'webapp:webapp',
		host='0.0.0.0',
		port=80,
		log_level='info',
		reload=True
	)
'''
