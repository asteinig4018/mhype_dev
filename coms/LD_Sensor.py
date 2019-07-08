import Sensor_Base
import logging as log
import serial

##################################################
'''
Laser Distance Senser

Creates an instance of a laser distance sensor
in terms of data aquisition. Ideally points to
a register in the future but will use Linux 
serial on Uartlite 1.
'''
##################################################

class LD_Sensor(Sensor_Base.Sensor_Base):
	
	def __init__(self, name):
		self.name = name

		#open uart port
		self.laser_dist_port = serial.Serial('/dev/ttyO5', baudrate=115200, timeout=.02, write_timeout=.02)
		self.laser_dist_port.close()
		self.laser_dist_port.open()
		if not laser_dist_port.isOpen():
    		log.info("ERROR 21: Laser Distance Sensor UART port was not opened properly")

		#reset buffers
		self.laser_dist_port.reset_input_buffer()
		self.laser_dist_port.reset_output_buffer()
		
		#start continuous update
		#TODO update to value for continuous
		self.laser_dist_port.write(b'/020D0e0C.')


	def get_data(self):
		#TODO check byte number
		s_in = self.laser_dist_port.read(14).decode('ascii')
		
		#parse

		return [self.name, s_in]