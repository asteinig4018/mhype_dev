##############################################
'''
Checksum 

Creates string of length 32 of a unique hash.
Identical data will generate the same hash
If someone is into crypto, implement a checksum.
For now this will work.
'''
##############################################
import hashlib
import json


#incoming data should be dictionary
def calculate(data):
	data_md5 = hashlib.md5(json.dumps(data)).hexdigest()
	return data_md5