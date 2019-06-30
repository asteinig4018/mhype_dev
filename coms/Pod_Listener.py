import Incoming_Message_Handler
import time

class Pod_Listener:

	def __init__(self):
		self.IMH = Incoming_Message_Handler()
		self.error_count = 0

	def run(self, ip = "192.168.1.25", port = 3000, timeout = 0):
		start_time = time.time()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bing((ip,port))

		while True:
			data, addr = self.sock.recvfrom(1024)
			msg = self.IMH.handle_message(data)
			if msg == None: #counter update
				continue
			if not msg:
				self.error_count +=1
				continue

			#cases for commands given to start threads and unpack data

			#all cases listed and managed

			#timeout condition
			elapsed_time = time.time() - start_time
			if timeout != 0 and elapsed_time > timeout:
				break