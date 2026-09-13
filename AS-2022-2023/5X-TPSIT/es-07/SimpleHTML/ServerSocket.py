import socket

# for url parser
import urllib.parse

HOST = '127.0.0.1'
PORT = 80
print(f'Start Server on port {PORT}..')
s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)

# if it's set on False the server will be shutdown
# for remote stopping
isWork = True
while isWork:
	con, addr = s.accept()
	# give from client her params
	head = con.recv(4096).decode().split('\n')[0]
	# give method url and ignore other code
	method, url, _ = head.split(' ')
	path = '/' if not f"{url.split('?')[0]}" else f"{url.split('?')[0]}"
	url = f'{url}?'.split('?')[1]
	params = urllib.parse.parse_qs(url)
	# if in your browser location you have ?end= param; the server will be stop
	isWork = 'end' not in params
	print(f'''
addr: {addr[0]}:{addr[1]}
method: {method}
path: {path}
GET: {params}
	''')
	# this is a tipical html response message
	con.send(f'''
HTTP/1.1 200 ok
Host: www.example.com
Accept-Language: it
Server: Python/3.11 (PythonOS@birg81)
Connection: close
Content-Type: text/html

<!doctype html>
<html lang="it">
<head>
<meta charset="UTF-8"/>
<title>🐍 Python</title>
</head>
<body>
<table>
<tr><th>addr</th><td>{addr[0]}:{addr[1]}</td></tr>
<tr><th>method</th><td>{method}</td></tr>
<tr><th>path</th><td>{path}</td></tr>
<tr><th>GET</th><td>{params}</td></tr>
<tr><th>Server work</th><td>{isWork}</td></tr>
</table>
</body>
</html>
'''.encode())

con.close()
print('Server Stopped..')