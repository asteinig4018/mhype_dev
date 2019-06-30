import Checksum
import Active_Counter
import json

'''
Incoming message handler

manages checksum, active counter, priority bytes
handler return types:
None - counter update message
False - msg error
json - data from message

to be implemented: smart counter window
'''

class Incoming_Message_Handler:

	def __init__(self):
		self.counter = Active_Counter.Active_Counter()


	#Pass incoming message as string
	def handle_message(self,message):
		#parse parts
		self.priority = message[:2]
		self.cksm = int(message[-16:])
		self.msg = message[2:-16]

		#calculate checksum
		calc_cksm = Checksum.calculate(self.msg)

		if(calc_cksm != cksm):
			return False

		#decode msg json
		msg_json = json.loads(self.msg)

		#handle update count message
		if(self.priority == '01'):
			new_count = int(msg_json["new_count"])
			self.counter.update_count(new_count)
			return

		#retrieve counter
		msg_count = int(msg_json["active_count"])

		#increment counter
		self.counter.increment()

		if(self.counter.check_value(msg_count)):
			return msg_json
		elif(self.priority == '00'): #allow emergency messages
			return msg_json
		else:
			self.counter.decrement()
			return False

