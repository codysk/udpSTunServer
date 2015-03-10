import thread
import sys
from socket import *
import struct
import time
import binascii

HOST = '192.168.0.98'  
PORT = 2333  
BUFSIZE = 1024 

data = struct.pack('>ccI',chr(0x00), chr(0x02), 0)

ADDR = (HOST, PORT)  
udpCliSock = socket(AF_INET, SOCK_DGRAM)
udpCliSock.sendto(data,ADDR)  
data,ADDR = udpCliSock.recvfrom(BUFSIZE)  
print binascii.b2a_hex(data)