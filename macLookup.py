#!/usr/bin/python

import subprocess
from time import time, sleep

# Define the users to lookup
users = ['Elias', 'Kevin', 'Nora', 'Inge', 'Bazzinga']
addr = ['38:ca:da:eb:3f:da', '2c:33:61:aa:e6:a9', 'cc:29:f5:b8:2d:a2', 'ac:5f:3e:28:2a:c0', 'f0:79:59:70:a4:a6']


def whosHome():
	# Get the output of the command 'arp-scan -l'
    arpOutput = subprocess.check_output("sudo arp-scan -l", shell=True).split('\n')
    # Strip away first three lines and last 5 lines
    arpOutput = arpOutput[2:-4] 

    # Open file times.txt and read lines to 'logFile'
    with open('/home/kevin/homeCheck/times.txt', 'r') as file:
	    logFile = file.readlines()

    i = 0
    # Go through each element in list 'addr'
    for mac in addr:
    	# Then iterate through each line in arpOutput
    	for line in arpOutput:
    		line_mac = str(line.split('\t')[1])

    		# For each line we check after a matching mac addr
    		if (mac in line_mac):
    			logFile[i] = str(users[i]) + ':' + str(time()) + '\n'
    			# print mac
    			# print users[i]
    			# print str(i) + '\n'
    			# print logFile

    	i+=1

    # Write changes to file
    with open('/home/kevin/homeCheck/times.txt', 'w') as file:
    	file.writelines(logFile)
    	print logFile


whosHome()
