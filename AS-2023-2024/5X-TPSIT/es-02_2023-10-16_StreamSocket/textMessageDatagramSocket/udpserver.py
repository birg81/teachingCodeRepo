import socket

HOST = '127.0.0.1'
PORT = 12345

# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))
print (f'UDP Server Llistening on PORT {PORT}..')

while True:
	# buffer size is 1024 bytes
	msg, addr = s.recvfrom(1024)
	print (f'{addr[0]}:{addr[1]}>> "{msg.decode('utf-8')}"...')