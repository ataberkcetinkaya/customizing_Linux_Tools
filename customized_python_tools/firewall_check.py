#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install wafw00f")
os.system("clear")
os.system("figlet Check  4  Firewalls")
print("""
A server-based tool that checks for firewalls

1) Firewall List
2) Firewall Detection

""")

operno = raw_input("Operation Number: ")

if operno == '1':
	os.system("wafw00f -l")
elif operno == '2':
	site = raw_input("Type Website: ")
	os.system("wafw00f " + site)
else:
	print("An error occurred. Try again.")
