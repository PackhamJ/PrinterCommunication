#Author Shivanshu Misra	
#
#
#

import socket
import random
import sys

# addressing and port information of a printer
IPADDR = '10.7.21.252'
PORTNUM = 35001

datasent2 = '\x2b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x6a\x5f\xf4\xcc' # in hexadecimal format
#Can send ASCII data also: ‘+.........j_’

# Establish a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect(s, IPADDR, PORTNUM):
        s.connect((IPADDR, PORTNUM))

#Send Hexadecimal data to printer at ip 10.7.21.252 to fetch logs as in TCP Stream
def senddata(s, datasent):
        s.send(datasent2)

#Receive logs from printer
def receivedata(s):
        chunk = []
        bytes_recvd = 0
        while True:
                # Receive no more than 1024 bytes and encode in ASCII format
                chunk = (s.recv(1024).encode("ascii","ignore"))
                if chunk == b'':
                        raise RuntimeError("socket connection broken")
                        for i in chunk:
                                chunk.append(i)
                bytes_recvd = bytes_recvd + len(chunk)
                print(chunk) #Printing data received from a printer
        return b''.join(chunk)

#Write data to an output file
def write_to_file(data):
        file = open("Output.txt", "w")
        for line in file:
                file.write(chunk)
        file.close()

def run():
        data = receivedata(s)
        write_to_file(data)

def closeconnection(s):
        s.close()

#Call all functions sequentially
connect(s, IPADDR, PORTNUM)
senddata(s, senddata)
receivedata(s)
run()
closeconnection(s)
printer-log-script.py
Open with
Displaying printer-log-script.py.