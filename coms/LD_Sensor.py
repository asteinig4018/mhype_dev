import Sensor_Base

##################################################
'''
Laser Distance Senser

Creates an instance of a laser distance sensor
in terms of data aquisition. Ideally points to
a register
'''
##################################################

class LD_Sensor(Sensor_Base.Sensor_Base):
	
	def __init__(self, name):
		self.name = name

	def get_data(self):
		pass
		