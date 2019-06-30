
'''
Function to send a counter update message

'''

def send_count_update(transmitter, new_count = 0):
	data = {"new_count": new_count }
	transmitter.send_message(data,'01', False)