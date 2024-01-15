import uvicorn
import mysql.connector as dbms
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

webapp = FastAPI(title = 'Test Login')

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

def getConnection():
	return dbms.connect(
		host = 'localhost', port = 3306,
		user = 'root', password = '',
		database = 'Login'
	)

@webapp.post('/login')
async def login(username: str, secret: str):
	con = getConnection()
	cur = con.cursor()
	cur.execute(f"SELECT * FROM Users WHERE username={username} AND secret={secret};")
	rs = cur.fetchall()
	cur.close()
	con.close()
	if len(rs) > 0:
		return RedirectResponse('./welcome.html')
	else:
		return RedirectResponse('./login.html')


if __name__ == '__main__':
	uvicorn.run(
		'main:webapp',
		host = '0.0.0.0',
		port = 3000,
		# use_colors = False,
		http = 'httptools',
		reload = True
	)