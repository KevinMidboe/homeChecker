#!/usr/bin/env python3
from socket import *
from macLookup import getTimes
import json
import logging
 
log = logging.getLogger(__name__)

# Define the socket communicating will transfered
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12001))

while True:
	try:
	  # Save the message and return address to variables.
	  message, address = serverSocket.recvfrom(1024)

	  print(message, address) # Debug print
	
	  times = json.dumps(getTimes())
	  # This should prob be cases and not if's, but works to get the right info user requests.
	  serverSocket.sendto(bytes(times, 'utf-8'), address)
#	  serverSocket.close()
	except Exception as e:
          log.info(e.message, e.args)
