#!/usr/bin/env python3
from socket import *
from macLookup import getTimes
import json

# Define the socket communicating will transfered
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12001))

while True:
	# Save the message and return address to variables.
	message, address = serverSocket.recvfrom(1024)

	print(message, address) # Debug print
	
	times = json.dumps(getTimes())
	# This should prob be cases and not if's, but works to get the right info user requests.
	serverSocket.sendto(bytes(times, 'utf-8'), address)

