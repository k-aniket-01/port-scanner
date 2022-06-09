
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
		print ("invalid Argument")
		
print("~^~" * 25)
print("scanning Target: " + target)
print("scanning started at: "+ str(datetime.now()))
print("~•~" * 25)

try:
	
	for port in range(1,1000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = s.connect_ex((target,port))
	if result == 0:
		print("port {} is open".format(port))
		s.colse()
		
except KeyboardInterrupt:
	print("\nexiting program!!!!!!!!")
	sys.exit()
except Socket.gaierror:
	print("\n hostname could not be resolved!!!!!!!" )
	sys.exit()
except socket.error:
	print("server not responding!!!!!")
	sys.exit()