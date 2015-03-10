import sys
import struct
import socket
import time
import Packet
import logging

onlineList = {}
def headerCut(byte):
	try:
		header = byte[0:2]
		header = struct.unpack(">cc",header)
		header = (ord(header[0]), ord(header[1]))
		pass
	except Exception, e:
		logging.info("InValid Header")
		header = (0x00, 0x00)
	#print header

	ret = {
		(0x00, 0x00): "NULL",
		(0x00, 0x01): "HELLO",
		(0x00, 0x02): "CONNECTREQ",
		(0x00, 0x03): "STATEQRY",
	}
	try:
		return (ret[header],byte[2:])
	except Exception, e:
		return (ret[(0x00, 0x00)],)

def hello_recv(byte, addr, socket_obj):
	try:
		(ipaddr, port, name) = struct.unpack(">IHI", byte)
	except Exception, e:
		logging.info("InValid body")
		return
		pass

	(Nipaddr, Nport) = addr;
	Nipaddr = socket.ntohl(struct.unpack('i',socket.inet_aton(Nipaddr))[0])
	Nipaddr = int(Nipaddr)
	timestamp = int(time.time())

#Block Existed ID
	if name in onlineList.keys():
		if onlineList[name][0] != ipaddr or \
		onlineList[name][1] != port or \
		onlineList[name][2] != Nipaddr or \
		onlineList[name][3] != Nport:
			if timestamp - onlineList[name][5] < 15:
				socket_obj.sendto(Packet.IDExisted().getBytes(), addr)
				return
				pass
			pass
		pass

	onlineList[name] = (ipaddr, port, Nipaddr, Nport, socket_obj, timestamp)
	logging.info(onlineList[name])
	socket_obj.sendto(Packet.helloRespond().getBytes(), addr)
	#return Packet.helloRespond().getBytes()

def connect_recv(byte, addr, socket_obj):
	try:
		(name,) = struct.unpack(">I", byte)
	except Exception, e:
		logging.info("InValid body")
		return
		pass

	if name not in onlineList.keys():
		socket_obj.sendto(Packet.DeviceNotFound().getBytes(), addr)
		return
		pass

	timestamp = int(time.time())

	if timestamp - onlineList[name][5] > 15:
		del onlineList[name]
		socket_obj.sendto(Packet.DeviceNotFound().getBytes(), addr)
		return
		pass

	Sip = socket.inet_ntoa(struct.pack('I',socket.htonl(onlineList[name][2])))
	Sport = onlineList[name][3]
	Saddr = (Sip, Sport)
	Ssocket_obj = onlineList[name][4]

	ip = socket.ntohl(struct.unpack('i',socket.inet_aton(addr[0]))[0])

	socket_obj.sendto(Packet.ConnectRespondToC(onlineList[name][0], onlineList[name][1], onlineList[name][2], onlineList[name][3], name).getBytes(), addr)
	Ssocket_obj.sendto(Packet.ConnectRespondToS(ip,addr[1]).getBytes(), Saddr)

	pass

def state_query_recv(byte, addr, socket_obj):
	try:
		(name,) = struct.unpack(">I", byte)
	except Exception, e:
		logging.info("InValid body")
		return
		pass

	if name not in onlineList.keys():
		socket_obj.sendto(Packet.DeviceNotFound().getBytes(), addr)
		return
		pass

	timestamp = int(time.time())

	if timestamp - onlineList[name][5] > 15:
		del onlineList[name]
		socket_obj.sendto(Packet.DeviceNotFound().getBytes(), addr)
		return
		pass

	socket_obj.sendto(Packet.DeviceOnline().getBytes(), addr)

	pass

def none(byte, addr, socket_obj):
	pass

def Process(byte, addr, socket_obj):
	(header, body) = headerCut(byte)
	do = {
		"NULL" : none,
		"HELLO" : hello_recv,
		"CONNECTREQ" : connect_recv,
		"STATEQRY" : state_query_recv,
	}
	do[header](body, addr, socket_obj)
	pass