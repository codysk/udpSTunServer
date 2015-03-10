import thread
import sys
from socket import *
import struct
import time
import binascii

HOST = '192.168.0.98'  
PORT = 2333  
BUFSIZE = 1024 

def send(addr, socket):
	data = struct.pack('>ccIHI',chr(0x00), chr(0x01), 3232235876, 1400, 0)
	while True:
		socket.sendto(data, addr)
		time.sleep(10)
		pass
	
	pass
def recv(socket):
	while True:
		data,addr = socket.recvfrom(BUFSIZE)
		print binascii.b2a_hex(data)
	pass

ADDR = (HOST, PORT)  
udpCliSock = socket(AF_INET, SOCK_DGRAM)
thread.start_new_thread(send, (ADDR,udpCliSock))
time.sleep(1)
recv(udpCliSock)