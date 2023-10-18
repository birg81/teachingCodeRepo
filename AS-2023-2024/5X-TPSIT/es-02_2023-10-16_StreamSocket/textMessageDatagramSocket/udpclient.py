import socket

HOST = '127.0.0.1'
PORT = 12345
MSG = input('(write your message) >_ : ').strip()

# UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MSG.encode('utf-8'), (HOST, PORT))

print (f'{HOST}:{PORT} (send) >> "{MSG}"..')
