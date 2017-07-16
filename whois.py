import pythonwhois
import json
import sys #sys.argv
import datetime
import yaml

def datetime_control(x):
    if isinstance(x, datetime.datetime): #isinstance type == datetime.datetime -> return x.isoformat()
        return x.isoformat() # HH:MM:SS

domainlist = sys.argv[1] #input domainlist

f = open(domainlist, 'r') # file open to read
while True: # loop
	line = f.readline() # read one line
	if len(line) == 0: #length of line == 0
		break
	whoiss = pythonwhois.get_whois(line) #whois information of one line
	my_json = json.dumps(whoiss, default = datetime_control, indent = 5) 
	#switch whoiss into json type and indent 4 and include datetime_handler function
	swichdic = yaml.load(my_json)
	#switch my_json to format yaml(json) 

	with open('whois.json', 'w')as make_file: #make file whois.json and write, if end task, close make_file 
 		json.dump(swichdic, make_file) # switch swichdic into json type.
		print swichdic #print swichdic

f.close() #file close