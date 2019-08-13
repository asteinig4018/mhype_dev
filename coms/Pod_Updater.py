import Transmitter
import time
import Data_Collector
import logging as log

#########################################################
'''
Pod Updater

This object is to be run in a seperate thread. It creates
an update for the base station using the data collector object
and a transmitter object to send the data. 
'''
#########################################################

class Pod_Updater:

	def __init__(self):
		self.transmitter = Transmitter.Transmitter("192.168.1.25", 8000, "192.168.1.21", 3000)
		self.data_collector = Data_Collector.Data_Collector()

		#initialize sensors
		#TODO write function that does this from .par file
		self.data_collector.add_LD_Sensor("uartlite_1")

	def get_data(self):
		#clear data dictionary
		self.data = {}
		#grab data from registers, as dictionary
		#self.data = self.data_collector.collect_data()
		#calculate major variables
		#package into json
		#add current count
		self.data['active_count'] = self.transmitter.get_count()

	def send(self):
		self.transmitter.send_message(self.data)

	def loop(self, timeout = 0.01):
		self.get_data()
		self.send()
		time.sleep(timeout)

	def run_update(self):
		try:
			while True:
				self.loop()

		finally:
			log.info("ending Updater")

		
