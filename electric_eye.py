#!/usr/local/bin python3

import os
import scapy.all as scapy
from pyfiglet import Figlet


def admin_check():
    # known good for MacOS, need to test Linux and Win32 will have its own.
    uid = os.getuid()
    if uid != 0:
        print('[-] Not and admin. Please run this command elevated using sudo.')
        exit()


def scan(ip):
    scapy.arping(ip)


admin_check()
custom_font = Figlet(font='cybermedium')
print(custom_font.renderText("Electric Eye"))
scan("192.168.1.1/24")
