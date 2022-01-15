#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet Compilation - berklinux")
print("""
Welcome to my compilation tool
""")

comp = raw_input("Type tool's name: ")

py_compile.compile(comp)
