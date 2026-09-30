from json import load
from random import choice
import socket

QUOTESNAME = 'motd.json'
with open(QUOTESNAME, 'r', encoding = 'utf-8') as f:
	quotes = load(f)

TEMPLATENAME = 'template.html'
with open(TEMPLATENAME, 'r', encoding = 'utf-8') as f:
	template = f.read()

HOST = '0.0.0.0'
PORT = 12345

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind((HOST, PORT))
ss.listen(1)
print(f'Server listening on http://{HOST}:{PORT}...')

goAway = True

while goAway:
	con, addr = ss.accept()
	req = con.recv(8192).decode('utf-8')
	print(f'{addr[0]}:{addr[1]} (recv) << Request recived')
	quote = choice(quotes)
	rendered_html = template.replace('{quote}', quote)
	res = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: {45 + len(rendered_html.encode('utf-8'))}
Connection: close

{rendered_html}""".replace('\r', '').replace('\n', '\r\n').encode('utf-8')
	con.send(res)
	con.close()
	print(f'{addr[0]}:{addr[1]} (send) >> Response HTTP "{quote}"')
	goAway = quote != 'end'

ss.close()
print('Server stopped...')
