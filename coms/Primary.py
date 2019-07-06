import Pod_Listener
import Pod_Updater

###################################################
'''
Primary code for the pod

Manages all primary threads and runs initialization
Also handles all keyboard input
'''
####################################################

def initialize():
	self.listener = Pod_Listener.Pod_Listener()
	self.updater = Pod_Updater.Pod_Updater()

def start():
	#do threads
	pass
	