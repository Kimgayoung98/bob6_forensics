import pythonwhois
import json
import sys
import datetime

def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")

filename = sys.argv[0]
if len(sys.argv) is 1:
	exit('Usage: ' + filename + ' filename')
domainlist = sys.argv[1]

f = open('url_sample.txt', 'r')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line
	whoiss = pythonwhois.get_whois(line)
	print whoiss
	with open('whois.txt', 'w')as make_file:
		my_json = json.dumps(whoiss, default = datetime_handler, indent = 4)
		print my_json

f.close()