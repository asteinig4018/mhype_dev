import Transmitter
import time
import Data_Collector

class Pod_Updater:

	def __init__(self):
		self.transmitter = Transmitter.Transmitter()
		data_collector = Data_Collector.Data_Collector()
		data_collector.add_LD_Sensor()

	def get_data(self):
		#clear data dictionary
		self.data = {}
		#grab data from registers, as dictionary
		self.data = data_collector.collect_data()
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

		
