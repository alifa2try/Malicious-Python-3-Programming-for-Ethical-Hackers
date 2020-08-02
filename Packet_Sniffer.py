#!/usr/bin/env python3

# This python tool will sniff packets from interface


# import modules
import argparse # for parsing over the terminal
import scapy.all as scapy # a module to enable us crafts packets
from scapy.layers.http import HTTPRequest 
from colorama import init, Fore

# initialize colorama
init() 

# define colors
red = Fore.RED
yellow = Fore.YELLOW
reset = Fore.RESET


# function to get interface to use for sniffing packets
def get_interface():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--interface", dest="interface", help="Specify an interface"
		                "to sniff packets from")
	option = parser.parse_args()

	if not option.interface:
		parser.error("Hey, buddy you surely need to specify an interface to get"
			        "the tool kicking!")
	else:
		return option.interface	


# A function to sniff packets from an interface 
def sniff_packets(interface):
	scapy.sniff(filter= "port 80", iface=interface, prn=analyze_packet, store=False)



def analyze_packet(packet):
	if packet.haslayer(HTTPRequest):
		url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
		print(f"{red}[+] Requested url >>> {url}\n\n{reset}")	

	if packet.haslayer(scapy.Raw):
		load = packet[scapy.Raw].load
		keywords = ['name', 'pass', 'login', 'user', 'email', 'username', 'password']

		for keyword in keywords:
			if keyword in str(load):
				print(f"{yellow}[+] Possible Credentials Detected >>> {load.decode()}\n\n{reset}")

		


interface = get_interface()
sniff_packets(interface)


