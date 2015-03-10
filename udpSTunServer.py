import sys,SocketServer,threading
import worker.Process
import logging
import thread

SERVER_PORT = 2333

class udpHandler(SocketServer.BaseRequestHandler):
	"""
	ACCEPT DATAGRAM
	"""
	def handle(self):
		(data, clientSocket) = self.request;
		try:
			respond = worker.Process.Process(data, self.client_address, clientSocket)
			pass
		except Exception, e:
			logging.warn(e)

		pass


def main():
#	print Port
	Server = SocketServer.ThreadingUDPServer(('', SERVER_PORT), udpHandler)
	
	Server.serve_forever()
	pass
if __name__ == '__main__':
	main()
