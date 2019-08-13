import Incoming_Message_Handler
import Command_Manager
import socket
import time
import logging as log

############################################################
'''
Pod Listener

On Pod object to be run in a thread that listens for incomming 
messages from the base station. Incoming messages are handled
first by the Incoming message handler and commands within those
messages are handled and carried out by the command manager.
'''
#############################################################

class Pod_Listener:

	def __init__(self, verbose = False):
		self.IMH = Incoming_Message_Handler.Incoming_Message_Handler(verbose)
		self.CM = Command_Manager.Command_Manager()
		self.error_count = 0
		self.verbose = verbose

	def vprint(self, output):
		if(self.verbose):
			log.info(output)

	def run_listen(self, ip = "192.168.1.25", port = 3000, timeout = 0):
		start_time = time.time()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((ip,port))

		#TODO add timeout
		try:
			while True:
				data, addr = self.sock.recvfrom(1024)
				msg = self.IMH.handle_message(data)
				if msg == None: #counter update
					continue
				if not msg: #error message
					self.error_count +=1
					continue

				#cases for commands given to start threads and unpack data
				self.CM.handle(msg)
				#all cases listed and managed

				#timeout condition
				elapsed_time = time.time() - start_time
				if timeout != 0 and elapsed_time > timeout:
					break
		finally:
			log.info("ending Listener")