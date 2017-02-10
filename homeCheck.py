#!/usr/bin/env python3

from socket import *
import json
from sys import argv

# Set host name and port
host = '10.0.0.41'
port = 12001

clientSocket = socket(AF_INET, SOCK_DGRAM)

def fetchHTimes(filter=None):
    clientSocket.sendto(b'get_times', (host, port))
    message, address = clientSocket.recvfrom(1024)
    message = message.decode('utf-8')
    
    for item in json.loads(message):
        if filter != None and item['name'].lower() == filter:
            print(item['name'].ljust(10) +': '+ item['time'])
            break
        elif filter == None:
            print(item['name'].ljust(10) +': '+ item['time'])
    clientSocket.close()

if __name__ == '__main__':
    if argv[-1][-3:] == '.py':
        fetchHTimes()
    else:
        fetchHTimes(argv[-1])