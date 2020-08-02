#!/usr/bin/env python3

# This is a python program that changes MAC address

#import modules
import argparse # to get arguments from the terminal
import subprocess # to enable us run system commands
import re # to use regular expression


# A function to get arguments from the terminal
def getArguments():
	parser = argparse.ArgumentParser() 
	parser.add_argument("-i", "--interface", dest="interface", help="Use this"
		                "option to specify the interface")
	parser.add_argument("-m", "--mac", dest="required_mac", help="Use this"
		                "option to specify the MAC address")
	options = parser.parse_args()

	if not options.interface:
		parser.error("[-] Please enter an interface")
	elif not options.required_mac:
		parser.error("[-] Please enter a MAC address")
	return options		


# A function to change the MAC address
def changeMAC(interface, mac):
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["sudo", "ifconfig", interface, "up"])


# A function to check MAC address
def checkMAC(interface):
	command_result=subprocess.check_output(["sudo", "ifconfig", interface])
	mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(command_result))
	
	if mac_address:
		return mac_address.group(0)
	else:
		print("[-] Couldn't get the MAC address")



# invoke getArgument() function
options = getArguments()

# print the current MAC address
print("The current MAC address is: ", checkMAC(options.interface))

#change MAC address
changeMAC(options.interface, options.required_mac)	

# print the new mac address
print("The new MAC address is: ", checkMAC(options.interface))
