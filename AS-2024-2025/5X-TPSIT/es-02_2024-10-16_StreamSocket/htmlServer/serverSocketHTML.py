import socket

HOST = '0.0.0.0'
PORT = 80

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST, PORT))
ss.listen(1)
print(f'Server listen on port: {PORT}...')
msg = f'''
HTTP/2.0 200 OK
Content-Type: text/html
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept
Access-Control-Allow-Methods: GET

<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Server HTML</title>
</head>
<body>
<h1>Server Socket</h1>
<p>HTML Stream Socket Server 🔌🌐</p>
</body>
</html>
	'''.strip().replace('\n','\r\n')
print(msg)
while True:
	con, addr = ss.accept()
	print(f'request from {addr[0]}:{addr[1]}')
	con.sendall(msg.encode('utf-8'))
	con.close()