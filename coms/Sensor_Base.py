import abc

'''
Base Sensor Class

All sensors classes should inherit this class to ensure
proper functionality.
'''

class Sensor_Base(abc.ABC):
	@abc.abstractmethod
	def get_data(self):
		pass