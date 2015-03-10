import sys
import struct

class helloRespond:
	"""helloRespond"""
	def __init__(self):
		self.bytes = struct.pack(">cc", chr(0x01), chr(0x01))
		pass
	def getBytes(self):
		return self.bytes

class ConnectRespondToC:
	"""ConnectRespondToC"""
	def __init__(self, ip, port, Nip, Nport, name):
		self.bytes = struct.pack(">ccIHIHI", chr(0x01), chr(0x02), ip, port, Nip, Nport, name)
		pass
	def getBytes(self):
		return self.bytes

class ConnectRespondToS:
	"""ConnectRespondToS"""
	def __init__(self, Nip, Nport):
		self.bytes = struct.pack(">ccIH", chr(0x01), chr(0x03), Nip, Nport)
		pass
	def getBytes(self):
		return self.bytes

class IDExisted:
	"""IDExisted"""
	def __init__(self):
		self.bytes = struct.pack(">cc", chr(0x03), chr(0x01))
		pass
	def getBytes(self):
		return self.bytes


class DeviceOnline:
	"""DeviceOnline"""
	def __init__(self):
		self.bytes = struct.pack(">cc", chr(0x03), chr(0x02))
		pass
	def getBytes(self):
		return self.bytes	

class DeviceNotFound:
	"""DeviceNotFound"""
	def __init__(self):
		self.bytes = struct.pack(">cc", chr(0x03), chr(0x03))
		pass
	def getBytes(self):
		return self.bytes		


if __name__ == '__main__':
	pack = helloRespond();
	depack = struct.unpack(">cc", pack.getBytes())
	print ord(depack[1])