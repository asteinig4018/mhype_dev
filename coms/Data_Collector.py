import LD_Sensor

class Data_Collector:

	def __init__(self):
		self.sensor_list = []




	#####  ADD Sensor Types Here ####
	def add_LD_Sensor(self):
		x = LD_Sensor(self)
		self.sensor_list.append(x)