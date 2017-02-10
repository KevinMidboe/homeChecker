from socket import *

# Define the socket communicating will transfered
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12001))

def readFile():
	with open('/home/kevin/homeCheck/times.txt', 'r') as content_file:
		content = content_file.read()
		return content

while True:
	# Save the message and return address to variables.
	message, address = serverSocket.recvfrom(1024)

	print(message, address) # Debug print

	# This should prob be cases and not if's, but works to get the right info user requests.
	if (message == 'get_times'):
		return_message = readFile()

	# Returns message to return address.
	serverSocket.sendto(return_message, address)
