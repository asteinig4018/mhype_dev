import abc

################################################
'''
Base Sensor Class

All sensors classes should inherit this class to ensure
proper functionality.
'''
##############################################

class Sensor_Base:
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_data(self):
		#returns [name, data]
		pass