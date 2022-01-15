#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install crunch")
os.system("clear")
os.system("figlet Create  your  own  Wordlist")
print("""
Welcome to the wordlist creater!
""")

mincharacter = raw_input("Min. character to use: ")
maxcharacter = raw_input("Max. character/s to use: ")
whichcharacters = raw_input("Characters to use: ")
savelocation = raw_input("Where to save: ")

os.system("crunch " + mincharacter + " " + maxcharacter + " " + whichcharacters + " -o " + savelocation)

print("\033[1;32;40m Done.")
