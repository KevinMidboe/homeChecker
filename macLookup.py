#!/usr/bin/env python3

import sqlite3
from subprocess import check_output, CalledProcessError
from time import time
from re import findall
from sys import argv
from pprint import pprint

def getOnlineClients():
    try:
        arpOutput = check_output("sudo arp-scan -l", shell=True)
        arpOutput = arpOutput.decode()
        
        macAdr = findall('(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))', arpOutput)
        return [i[0] for i in macAdr]

    except CalledProcessError:
        print("Not able to run 'arp-scan -l' on this machine.")
        exit(0)

def getAddr(c):
    c.execute('SELECT adr FROM clients')
    
    return [i[0] for i in c.fetchall()]

def getTimes():
    conn = sqlite3.connect('home.db')
    c = conn.cursor()

    c.execute('SELECT c.name, l.timesince FROM lastonline AS l JOIN clients AS c WHERE l.clientadr=c.adr')

    returnList = []
    for name, time in c.fetchall():
        returnList.append({"name": name, "time": convertTime(time)})

    conn.close()

    return returnList

def convertTime(seconds):
    delta = time() - seconds
    if delta >= 86400:
        return str(delta//86400) + ' days'
    elif delta >= 3600:
        if delta//3600 < 10:
            parent = str(delta//3600)
            child = str((delta - (3600 * (delta//3600)))//60)
            if len(child) == 1:
                child = '0' + child
            return parent + ':' + child + ' hours'
        else:
            return str(delta//3600) + ' hours'
    elif delta >= 60:
        return str(delta//60) + ' minutes'
    else:
        return str(delta) + ' seconds'


def updateTimes():
    curTime = time()
    conn = sqlite3.connect('home.db')
    c = conn.cursor()
    
    online = list(set(getOnlineClients()) & set(getAddr(c)))

    for adr in online:
        c.execute('UPDATE lastonline SET timesince='+ str(curTime) +' WHERE clientadr="'+ adr + '"')

    conn.commit()
    conn.close()

    return (online)

if __name__ == '__main__':
    if argv[-1] == 'add':
        print("Updated following clients:", updateTimes())
    elif argv[-1] == 'get':
        pprint(getTimes())
    else:
        print("Add args 'add' or 'get'")

    

