import socket

HOST = '127.0.0.1'
PORT = 12345

s = socket.socket()		# socket.AF_INET, socket.SOCK_STREAM)

print(f'TCP Server Listening on {HOST}:{PORT}..')

s.bind((HOST, PORT))
s.listen(1)

isWorking = True
while isWorking:
	con, addr = s.accept()
	msg = con.recv(16).decode()
	print (f'[{addr[0]}:{addr[1]}] << "{msg}"...')
	isWorking = 'end' not in msg.lower()

con.close()
print('Server Stopped..')
