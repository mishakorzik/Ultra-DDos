import os
import time
import random
import sys

os.system("clear")
os.system("python src/logo.py")
os.system("python src/serv.py")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

g="\033[1;32m"
r="\033[1;31m"
w="\033[0m"
b="\033[1;34m"
o="\033[1;33m"
bl="\033[1;36;40m"

print("1. DDos Ip Address")
print("2. Wiev Url Ip Address")
print("3. DDos site logs")
op=int(raw_input("Options: "))
if(op==1):
 os.system("python2 src/ddos.py")
elif(op==2):
 os.system("python src/Url.py")
elif(op==3):
 os.system("python src/log-ddos.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools!") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd Ultra-DDos")
 os.system("python2 main.py")
