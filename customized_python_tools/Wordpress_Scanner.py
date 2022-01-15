#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet WordPRess Scanner BerkLinux")
print("""
Scan the sites that based on Wordpress.

1) Quick Scan
2) Add-On Scan
3) Theme Scan
4) Administrator Scan
""")

operno = raw_input("Choose: ")

if operno == '1':
	site = raw_input("Type the site: ")
	os.system("wpscan --url " + site)
elif operno == '2':
	site = raw_input("Type the site: ")
	os.system("wpscan --url " + site + " --enumerate p")
elif operno == '3':
	site = raw_input("Type the site: ")
	os.system("wpscan --url " + site + " --enumerate t")
elif operno == '4':
	site = raw_input("Type the site: ")
	os.system("wpscan --url " + site + " --enumerate u")
else:
	print("\033[1;31;40m An error occured. Please try again.")
