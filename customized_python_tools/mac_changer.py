#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install macchanger")
os.system("clear")
os.system("figlet Mac - Changer / Berk")

print("""
Change your Mac easily...

1) Random Mac Address
2) Add Your Mac Address Manually
3) Back to My Normal Mac Address

ps: Works on your eth0 ethernet card.
""")

operno = raw_input("Choose Operation: ")

if operno == '1':
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[092m New Mac Address is now ready to use.")
	
elif operno == '2':
	macaddress = raw_input("Type your new Mac Address: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macaddress + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[092m Your new mac manually configured and now ready to use.")
	
elif operno == '3':
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[092m Back to your original mac now.")
	
else:
	print("\33[1;33;40m An error occurred. Please try again.")
	
	
	
