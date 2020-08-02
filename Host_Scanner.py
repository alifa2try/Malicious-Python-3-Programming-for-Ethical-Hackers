#!/usr/bin/env python3

# This program will scan a target network and gets all the hosts attached to it


# import modules
import argparse # to get options over the terminal
import scapy.all as scapy # for packet crafting

# a function to get target over the terminal
def get_target():
	parser = argparse.ArgumentParser() # instantiate an object 
	parser.add_argument("-t", "--target", dest="target", help="Specify a target"
	                   " to scan")
	option = parser.parse_args() # parse over the terminal

	# check to see that the user has entered an option
	if not option.target:
		parser.error("Hey, buddy you need to specify a target to get" 
			         " the tool kicking")
		raise SystemExit
	else:
		return option.target	


# a function to scan the  network
def scan_target(target):
	arp_request = scapy.ARP(pdst=target) # instantiates an object of class ARP (ARP packet)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast_arp_request = broadcast/arp_request
	answered_list=scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
	
	host_list = [] # creates an empty list
	for packet in answered_list:
		host_dict = {"ip":packet[1].psrc, "mac":packet[1].hwsrc}
		host_list.append(host_dict)
	return host_list	


# A function to print out the hosts	
def print_hosts(hosts):
	print("IP Address\t\t\tMAC Address" )

	for host in hosts:
		print(host["ip"] + "\t\t\t" + host["mac"] )



target=get_target()		
hosts=scan_target(target)
print_hosts(hosts)

