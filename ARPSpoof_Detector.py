#!/usr/bin/env python3


# A python program to detect ARP spoofing

import scapy.all as scapy
import sys
from colorama import Fore, init

Green = Fore.GREEN
Red = Fore.RED
Reset = Fore.RESET

init()


def display_banner():
    banner = '''
    

8""""8                        8""""8                                         
8      eeeee eeeee eeeee eeee 8    8 eeee eeeee eeee eeee eeeee eeeee eeeee  
8eeeee 8   8 8  88 8  88 8    8e   8 8      8   8    8  8   8   8  88 8   8  
    88 8eee8 8   8 8   8 8eee 88   8 8eee   8e  8eee 8e     8e  8   8 8eee8e 
e   88 88    8   8 8   8 88   88   8 88     88  88   88     88  8   8 88   8 
8eee88 88    8eee8 8eee8 88   88eee8 88ee   88  88ee 88e8   88  8eee8 88   8 

Detect and report ARP Spoofing Attack
By F@ys@l G@m@, Pho3nyx Ac@demy. 

Github : https://github.com/alifa2try
Contact : faysal@phoenyxacademy.com 
    
    '''
    print(f"{Green}{banner}{Reset}")


def get_interface():
    try:
        iface = sys.argv[1]
    except IndexError:
        iface = conf.iface
    
    return iface    
    

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  

    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(filter="ARP", iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print(f"{Red}[-] You are under attack!{Reset}")
        except IndexError:
            pass


# program's main body
display_banner()

iface = get_interface()

sniff(iface)

