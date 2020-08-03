#!/usr/bin/env python3

# A port Simple port scanner


# import modules
import argparse # to get options from the terminal
import scapy.all as scapy # for packet crafting
import prettytable # for tabular output
from colorama import Fore # color text formatting



# define colorama colors
Green = Fore.GREEN
Red = Fore.RED
Cyan = Fore.CYAN
Reset = Fore.RESET
Yellow = Fore.YELLOW

def display_banner():
	banner_text = '''

8""""8                   8""""8                                    
8    8 eeeee eeeee eeeee 8      eeee eeeee eeeee eeeee eeee eeeee  
8eeee8 8  88 8   8   8   8eeeee 8  8 8   8 8   8 8   8 8    8   8  
88     8   8 8eee8e  8e      88 8e   8eee8 8e  8 8e  8 8eee 8eee8e 
88     8   8 88   8  88  e   88 88   88  8 88  8 88  8 88   88   8 
88     8eee8 88   8  88  8eee88 88e8 88  8 88  8 88  8 88ee 88   8 

PortScanner v1.0
Coded by Faisal Gama
Phoenyx Academy
faysal@phoenyxacademy.com

	'''
	print(f"{Yellow}{banner_text}{Reset}")


# get arguments from the terminal  
def get_arguments():
	parser = argparse.ArgumentParser(description=display_banner())
	
	# positional argument
	parser.add_argument("target", help="Target to perform a scan on")
	parser.add_argument("scan", help="Specify scan type: TCP|SYN|XMAS|UDP|FIN|NULL|ACK|WIND")

	# optional arguments
	parser.add_argument("-p", "--port", dest="port", type=int, 
						help="Specify a single port to scan")
	parser.add_argument("-pl", "--port-list", dest="ports_list", 
						help="Specify a ports list to scan, separated by a comma "
						"e.g. 20,30,40")
	parser.add_argument("-pr", "--port-range", dest="ports_range", 
						help="Specify ports range to scan, e.g. 40-100")
	
	

	# get the arguments from the terminal
	option = parser.parse_args() # parse over the terminal

	return option	


def set_ports():
	a_ports_list_to_return = []

	if option.port:
		a_ports_list_to_return.append(option.port)
		
	if option.ports_list:
		ports = option.ports_list.split(',')
		a_ports_list_to_return += ports
		

	if option.ports_range:
		ports = option.ports_range.split('-')	
		lower_bound = int(ports[0])
		upper_bound = int(ports[1])
		ports_range = range(lower_bound, upper_bound + 1, 1)
		a_ports_list_to_return += ports_range
		

	place_holder_list = []

	for element in a_ports_list_to_return:
		place_holder_list.append(int(element))	

	a_ports_list_to_return = list(set(place_holder_list))

	a_ports_list_to_return.sort()

	if not len(a_ports_list_to_return) > 0:
		print("[-] You need to enter a port to scan. Enter -h for help")
		raise SystemExit 		 	

	return a_ports_list_to_return


def tcp_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='S')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 18:
				ip_reset_packet = scapy.IP(dst=target)
				tcp_reset_packet = scapy.TCP(sport=source_port, dport=port, flags='RA')
				reset_packet = ip_reset_packet/tcp_reset_packet
				reset_response = scapy.sr1(reset_packet, timeout=1, verbose=False)
				return "Open"
			elif scan_response[scapy.TCP].flags == 20:
				return "Closed"	
	else:
		return "Filtered"
	

def syn_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='S')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 18:
				ip_reset_packet = scapy.IP(dst=target)
				tcp_reset_packet = scapy.TCP(sport=source_port, dport=port, flags='R')
				reset_packet = ip_reset_packet/tcp_reset_packet
				reset_response = scapy.send(reset_packet, verbose=False)
				return "Open"
			elif scan_response[scapy.TCP].flags == 20:
				return "Closed"	
	else:
		return "Filtered"


def xmas_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='FPU')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 20:
				return "Closed"
			elif int(scan_response[scapy.ICMP].type) == 3 and int(scan_response[scapy.ICMP].code) in [1, 2, 3, 9, 10, 13]:
				return "Filtered"	
	else:
		return "Open|Filtered"


def fin_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='F')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 20:
				return "Closed"
			elif int(scan_response[scapy.ICMP].type) == 3 and int(scan_response[scapy.ICMP].code) in [1, 2, 3, 9, 10, 13]:
				return "Filtered"	
	else:
		return "Open|Filtered"


def null_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 20:
				return "Closed"
			elif int(scan_response[scapy.ICMP].type) == 3 and int(scan_response[scapy.ICMP].code) in [1, 2, 3, 9, 10, 13]:
				return "Filtered"	
	else:
		return "Open|Filtered"	

def ack_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='A')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 4:
				return "Unfiltered"
			elif int(scan_response[scapy.ICMP].type) == 3 and int(scan_response[scapy.ICMP].code) in [1, 2, 3, 9, 10, 13]:
				return "Filtered"
	else:
		return "Filtered"


def window_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	tcp_scan_packet = scapy.TCP(sport=source_port, dport=port, flags='A')
	scan_packet = ip_scan_packet/tcp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
		
	if scan_response != None:
		if scan_response.haslayer(scapy.TCP):
			if scan_response[scapy.TCP].flags == 4 and int(scan_response[scapy.TCP].window) > 0:
				return "Open"
			elif scan_response[scapy.TCP].flags == 4 and int(scan_response[scapy.TCP].window) == 0:
				return "Closed"
	else:
		return "Filtered"


def udp_scan(target, port):
	source_port = scapy.RandShort() 
	ip_scan_packet = scapy.IP(dst=target)
	udp_scan_packet = scapy.UDP(sport=source_port, dport=port)
	scan_packet = ip_scan_packet/udp_scan_packet
	scan_response = scapy.sr1(scan_packet, timeout=1, verbose=False)
	
		
	if scan_response != None:
		if scan_response.haslayer(scapy.UDP):
			return "Open"
		elif int(scan_response[scapy.ICMP].type) == 3 and int(scan_response[scapy.ICMP].code) == 3:
			return "Closed"
		elif int(scan_response[scapy.ICMP].type) == 3 and int(scan_response[scapy.ICMP].code) in [1, 2, 9, 10, 13]:	
			return "Filtered"
	else:
		return "Open|Filtered"


def specify_scan_type(scan_type, target, ports):
	results_dict = {} 

	if scan_type == 'TCP':
		for port in ports:
			scan_result = tcp_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	

	elif scan_type == 'SYN':
		for port in ports:
			scan_result = syn_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	
	

	elif scan_type == 'XMAS':
		for port in ports:
			scan_result = xmas_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	
			

	elif scan_type == 'FIN':
		for port in ports:
			scan_result = fin_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	
			
	
	elif scan_type == 'NULL':
		for port in ports:
			scan_result = null_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	

	elif scan_type == 'ACK':
		for port in ports:
			scan_result = ack_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	

	elif scan_type == 'WIND':
		for port in ports:
			scan_result = window_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	


	elif scan_type == 'UDP':
		for port in ports:
			scan_result = udp_scan(target, port)
			results_dict[port] = scan_result
		print_scan_result(results_dict, scan_type, target)	


	else:
		print("[-] Unsupported scan type, enter -h for help")								


def print_scan_result(results_dict, scan_type, target):
	print(f"\n\n{Green}[+] {scan_type} scan result for {target}{Reset}\n")

	x = prettytable.PrettyTable(["PORT", "STATE"])

	for port in results_dict:
		x.add_row([port, results_dict[port]])
	print(f"{Cyan}{x}{Reset}")

	print(f"\n{Green}[+] {scan_type} scan result for {target} completed{Reset}")




# main body
option = get_arguments()
ports = set_ports()

specify_scan_type(option.scan, option.target, ports)

