import Checksum
import Active_Counter
import json
import socket

'''
Transmitter Object

Message layout: 2 byte priotiy, data, 16 byte checksum 
Includes active counter handling
'''

class Transmitter:

	def __init__(self, ip="192.168.1.21", port=3000, rxip="192.168.1.25", rxport=3000):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((ip, port))
		self.rxip = rxip
		self.rxport = rxport
		self.counter = Active_Counter.Active_Counter()

	def send_message(self, data, priority = '11', count_incr = True):
		cksm = Checksum.calculate(data)
		message = priority + json.dumps(data) + cksm
		try:
			self.sock.sendto(message, (rxip, rxport))
		#TODO implement catch, fail, etc
		if(count_incr):
			self.counter.increment()

	def get_count(self):
		return self.counter.get_count()

	def update_count(self, new_count):
		self.counter.update_count(new_count)


