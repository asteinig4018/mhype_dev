import Incoming_Message_Handler
import Command_Manager
import time

class Pod_Listener:

	def __init__(self, logfile = 0):
		self.IMH = Incoming_Message_Handler.Incoming_Message_Handler()
		self.CM = Command_Manager.Command_Manager()
		self.error_count = 0
		if(logfile != 0):
			pass #todo

	def run(self, ip = "192.168.1.25", port = 3000, timeout = 0):
		start_time = time.time()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((ip,port))

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