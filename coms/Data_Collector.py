import LD_Sensor

class Data_Collector:

	def __init__(self):
		self.sensor_list = []

	def collect_data(self):
		#empty dictionary
		data = {} 
		for sensor in sensor_list:
			pkg = sensor.get_data()
			data[pkg[0]] = pkg[1]

		return data


	#####  ADD Sensor Types Here ####
	def add_LD_Sensor(self):
		x = LD_Sensor(self)
		self.sensor_list.append(x)