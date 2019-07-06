
##################################################################
'''
Command Manager

Takes incoming messages that are not counter updates and 
handles them. Incoming messages could be:
- heartbeat
- motion-related command
- break/abort

If necessary, a new thread will be started to carry out the command
'''
##################################################################

class Command_Manager:

	def __init__(self):
		pass

	def handle(self, msg):#msg is json
		pass
