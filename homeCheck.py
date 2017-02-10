#!/usr/bin/env python3

from socket import *
from pprint import pprint
import json

# Set host name and port
host = '10.0.0.41'
port = 12001

clientSocket = socket(AF_INET, SOCK_DGRAM)

def main():
    clientSocket.sendto(b'get_times', (host, port))
    message, address = clientSocket.recvfrom(1024)
    message = message.decode('utf-8')
    for item in json.loads(message):
        print(item['name'].ljust(10) + ': ' + item['time'])
    clientSocket.close()

if __name__ == '__main__':
    main()