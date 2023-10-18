# Import the 'socket' module for network communication.
import socket

# Define the host IP address and port number to connect to.
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the specified host and port.
s.connect((HOST, PORT))

# Prompt the user to input a message.
MSG = input('(write your message) >_ : ').strip()

# Encode the message to UTF-8 and send it to the server.
s.send(MSG.encode('utf-8')

# Print the host and port to which the message is sent, along with the message itself.
print(f'{HOST}:{PORT} (send) >> "{MSG}"..')

# Receive a response message (up to 1024 bytes) from the server, decode it from UTF-8, and remove leading/trailing whitespace.
MSG = s.recv(1024).decode('utf-8').strip()

# Print the host and port from which the response is received, along with the response message.
print(f'{HOST}:{PORT} (recv) << "{MSG}"..')

# Close the socket connection.
s.close()