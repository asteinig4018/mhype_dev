import Transmitter
import time

class Pod_Updater:

	def __init__(self):
		self.transmitter = Transmitter.Transmitter()

	def get_data(self):
		#grab data from registers
		#calculate major variables
		#package into json
		#add current count
		self.data["active_count"]:self.transmitter.get_count()

	def send(self):
		self.transmitter.send_message(self.data)

	def loop(self, timeout = 0.01):
		get_data()
		send()
		time.sleep(timeout)

		
