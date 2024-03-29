import Pod_Listener
import Pod_Updater
import threading
import time

###################################################
'''
Primary code for the pod

Manages all primary threads and runs initialization
Also handles all keyboard input
'''
####################################################

class Primary:

	def __init__(self):
		listener = Pod_Listener.Pod_Listener(True)
		updater = Pod_Updater.Pod_Updater()
		self.updaterThread = threading.Thread(target= updater.run_update)
		self.listenerThread = threading.Thread(target=listener.run_listen)

	def start(self, timeout=100):
		#do threads
		self.updaterThread.start()
		#self.listenerThread.start()
		print "thread started"
		#timeout
		time.sleep(timeout)

		print "end"
		self.updaterThread.join()
		#self.listenerThread.join()

try:
	primary = Primary()
	primary.start()
except KeyboardInterrupt:
	raise	