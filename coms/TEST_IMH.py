#Unit test - Incoming Message Handler
import Incoming_Message_Handler
import Checksum
import json
import logging as log
log.basicConfig(filename='example1.log',level=log.DEBUG)
imh = Incoming_Message_Handler.Incoming_Message_Handler(True)

msg = {
	"active_count":2,
	"yaw_x" : -5,
	"abort" : False,
	"speed" : 25.6
}

msg2 = {
	"hello": "world"
}

msg3 = {
	"active_count":2,
	"yaw_x" : -5,
	"abort" : False,
	"speed" : 25.6,
	"hello": "world",
	"more_data": 23235
}

print msg

chksm = Checksum.calculate(msg)

print Checksum.calculate(msg2)
print Checksum.calculate(msg3)	
print chksm
print len(chksm)
log.info('test')

message = '11' + json.dumps(msg) + chksm 
print message

x = imh.handle_message(message)

print x
print x['abort']