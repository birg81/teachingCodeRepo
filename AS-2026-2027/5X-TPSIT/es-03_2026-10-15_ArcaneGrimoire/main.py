from json import load, dumps
import socket
GRIMOIRE_INGREDIENTS = './ingredients.json'
with open(GRIMOIRE_INGREDIENTS, 'r', encoding = 'utf-8') as f:
	grimoire = load(f)

grimoire.append({
	"id": 99,
	"name": "Professorial Coffee Bean of Infinite Debugging",
	"description": "A legendary, pitch-black coffee bean roasted in ancient server rooms. It grants the consumer absolute focus to spot a missing semicolon hidden across a thousand lines of code.",
	"earth": 2,
	"water": 1,
	"fire": 5,
	"air": 4
})

grimoire2str:str = dumps(grimoire, indent = 0, ensure_ascii = False, separators = (',', ':'))

HOST = '0.0.0.0'
PORT = 8080

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ss.bind((HOST, PORT))
ss.listen(1)
print(f'Server listening on http://{HOST}:{PORT}...')

res = f"""HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS
Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With
Access-Control-Allow-Credentials: true
Connection: close

{grimoire2str}""".replace('\r', '').replace('\n', '\r\n').encode('utf-8')

goAway = True
while goAway:
	con, addr = ss.accept()
	req = con.recv(4096).decode('utf-8')
	print(f'{addr[0]}:{addr[1]} (recv) << Request received')
	con.send(res)
	con.close()
	print(f'{addr[0]}:{addr[1]} (send) >> Response JSON DATA')

ss.close()
print('Server stopped...')
