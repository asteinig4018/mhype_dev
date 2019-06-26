######################################
'''
Active Counter with set rolling window (not controled or dynamic)

'''
#####################################

class Active_Counter:
	#initialization to 0 count
	def __init__(self):
		self.counter = 0
		#window is now (0,1,2)
		self.max = 3


	#increments counter and shifts window
	def increment(self):
		self.counter += 1
		self.max += 1

	#set new window width
	def set_window(self, new_width):
		self.max = counter + new_width

	#check a value
	def check_value(self, value):
		if value >= self.counter and value < self.max:
			return True
		else:
			return False

	#update on recieving auth counter
	def update_count(self, new_count):
		diff = self.max - self.counter
		self.counter = new_count
		self.max = self.counter + diff
		return self.counter
