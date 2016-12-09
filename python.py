#!/usr/bin/python

import requests

url = 'http://acadmin/findMyBCD.php'
BSNs = ['8FA000001F4B3', '846000123E71F', '84600013415B']
payload = {'bsn': '8FA000001FBA3'}

success_str = "is connected"
failure_str = "could not find"

for BSN in BSNs:
	# POST with form-encoded data
	r = requests.post(url, data={'bsn':BSN} )
	
	# Response, status etc
	# print r.text
	# print r.status_code
	
	if r.text.find(success_str) > 0:
		print BSN + ":" + "Connected"
		print "\n"
		
	if r.text.find(failure_str) > 0:
		print BSN + ":" + "Not Connected"
		print "\n"