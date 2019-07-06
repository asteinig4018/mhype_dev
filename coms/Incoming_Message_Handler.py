import Checksum
import Active_Counter
import json
import logging as log

'''
Incoming message handler

manages checksum, active counter, priority bytes
must be used with some kind of message udp receiver

handler return types:
None - counter update message
False - msg error
json - data from message

Priority bytes:
00 - emergency (ex. braking)
01 - counter sync
11 - regular traffic

to be implemented: smart counter window
'''

class Incoming_Message_Handler:

	def __init__(self, verbose = False):
		self.counter = Active_Counter.Active_Counter()
		self.verbose = verbose
		log.basicConfig(level=log.DEBUG)

	#verbose print function
	def vprint(self, output):
		if(self.verbose):
			log.info(output)


	#Pass incoming message as string
	def handle_message(self,message):
		#parse parts
		self.priority = message[:2]
		self.cksm = message[-32:]
		self.msg = message[2:-32]

		self.vprint(self.msg)

		#calculate checksum
		calc_cksm = Checksum.calculate(json.loads(self.msg))

		self.vprint("Calculated checksum: " + str(calc_cksm))
		self.vprint("Delivered checksum: " + str(self.cksm))

		if(calc_cksm != self.cksm):
			return False

		#decode msg json
		msg_dict = json.loads(self.msg)

		#handle update count message
		if(self.priority == '01'):
			new_count = int(msg_dict["new_count"])
			self.counter.update_count(new_count)
			return

		#retrieve counter
		msg_count = int(msg_dict["active_count"])
		self.vprint("Active Count: " + str(msg_count))

		#increment counter
		self.counter.increment()

		if(self.counter.check_value(msg_count)):
			return msg_dict
		elif(self.priority == '00'): #allow emergency messages
			return msg_dict
		else:
			self.counter.decrement()
			return False

