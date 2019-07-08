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
		listener = Pod_Listener.Pod_Listener()
		updater = Pod_Updater.Pod_Updater()
		self.updaterThread = threading.Thread(target= updater.run)
		self.listenerThread = threading.Thread(target=listener.run)

	def start(self, timeout=10):
		#do threads
		self.updaterThread.start()
		self.listenerThread.start()

		#timeout
		time.sleep(timeout)

		self.updaterThread.join()
		self.listenerThread.join()
	