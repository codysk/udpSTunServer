import thread
import sys
from socket import *
import struct
import time
import binascii

HOST = '192.168.0.98'  
PORT = 2333  
BUFSIZE = 1024 

data = struct.pack('>IIIIIIIII',1,1,1,1,1,1,1,1,1)

ADDR = (HOST, PORT)  
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.sendto(data,ADDR)  
#data,ADDR = udpCliSock.recvfrom(BUFSIZE)  
print binascii.b2a_hex(data)