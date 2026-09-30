# Import the 'socket' module for network communication.
import socket

# Define the host IP address and port number.
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object.
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port.
ss.bind((HOST, PORT))

# Listen for incoming connections with a maximum of 1 connection in the queue.
ss.listen(1)

# Print a message indicating the server is listening on a specific port.
print(f'Server listen on port: {PORT}...')

# Initialize a flag to control the server loop.
goAway = True

# Start a loop to handle incoming client connections.
while goAway:
	# Accept an incoming connection and get the connection object and client address.
	con, addr = ss.accept()

	# Receive a message (up to 1024 bytes), decode it from UTF-8, and remove leading/trailing whitespace.
	MSG = con.recv(1024).decode('utf-8').strip()

	# Print the client's IP and port along with the received message.
	print(f'{addr[0]}:{addr[1]} (recv) << "{MSG}"..')

	# Check if the received message, when converted to lowercase, is 'end' to exit the loop.
	goAway = MSG.lower() != 'end'

	# Reverse the received message.
	MSG = MSG[::-1]

	# Send the reversed message back to the client after encoding it in UTF-8.
	con.send(MSG.encode('utf-8'))

	# Print the client's IP and port along with the sent message.
	print(f'{addr[0]}:{addr[1]} (send) >> "{MSG}"..')

	# Close the connection with the current client.
	con.close()

# Close the main server socket.
ss.close()

# Print a message indicating that the server was remotely stopped.
print('Server was remote stopped...')