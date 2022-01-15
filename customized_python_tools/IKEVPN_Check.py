#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install ike-scan")
os.system("clear")
os.system("figlet IKE-VPN Checker")

print("""
Welcome to IKE-VPN Checker!!!

ps: its only detects IKE-VPN protocols.
""")

targetip = raw_input("Target IP: ")

os.system("ike-scan " + targetip)
