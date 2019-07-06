##############################################
'''
Checksum (creates string of length 32)
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