#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install nmap")
os.system("clear")
os.system("figlet Berk s Port Scan")
print(""" 
Created by Berk.

1) Fast Scan
2) Service n Version Info
3) OS Info
""")

operno = raw_input("Select Operation: ")

if operno == "1":
	targetip = raw_input("Target IP: ")
	os.system("nmap " + targetip)
elif operno == "2":
	targetip = raw_input("Target IP: ")
	os.system("nmap -sS -sV " + targetip)
elif operno == "3":
	targetip = raw_input("Target IP: ")
	os.system("nmap -O " + targetip)
else:
	print("An error occurred. Please try again.")
