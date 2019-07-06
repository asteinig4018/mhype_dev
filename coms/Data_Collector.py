import LD_Sensor

###################################################
'''
Data Collector

Manages getting all data from all sensors.
All sensors should be derived from the Sensor_Base
class. Sensor will have to be setup.
'''
####################################################

class Data_Collector:

	def __init__(self):
		self.sensor_list = []

	def collect_data(self):
		#empty dictionary
		data = {} 
		for sensor in self.sensor_list:
			pkg = sensor.get_data()
			data[pkg[0]] = pkg[1]

		return data


	#####  ADD Sensor Types Here ####
	#TODO setup via .par file
	def add_LD_Sensor(self, name):
		x = LD_Sensor.LD_Sensor(name)
		self.sensor_list.append(x)