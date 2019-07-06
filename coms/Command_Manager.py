import logging as log

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

	def __init__(self, verbose = False):
		self.verbose = verbose

	#verbose print function
	def vprint(self, output):
		if(self.verbose):
			log.info(output)

	def handle(self, msg):#msg is dictionary
		if msg['type'] == 'heartbeat':
			#compare timestamp difference to parameter
			#update variable
			pass

		elif msg['type'] == 'abort':
			#do abort
			pass

		elif msg['type'] == 'brake':
			#do brake
			pass

		elif msg['type'] == 'motion':
			#carry out motion - path with stop point, not just forward
			pass
		#For debugging purposes
		elif msg['type'] == 'debug':
			print msg['pkg']
		
