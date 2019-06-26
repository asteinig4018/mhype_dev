import Checksum
import json
import time
import struct
import socket

class Transmitter:

	def __init__(self, ip="192.168.1.21", port=3000, rxip="192.168.1.25", rxport=3000):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((ip, port))
		self.rxip = rxip
		self.rxport = rxport

	def send_message(self, data):
		cksm = Checksum.calculate(data)
		message = json.dumps(data) + cksm
		self.sock.sendto(message, (rxip, rxport))


