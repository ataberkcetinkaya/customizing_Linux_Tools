#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("sudo apt-get install figlet")
os.system("sudo apt-get install chkrootkit")
os.system("clear")
os.system("figlet R00tK1T Sc4nn3r - B3rkL1nux")
print("Scans for the rootkits")

os.system("chkrootkit")

print("\033[1;33;40m Scan completed. Check for results.")
