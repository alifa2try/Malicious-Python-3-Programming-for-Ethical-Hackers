#!/usr/bin/env python3

# This program crawls websites


# import modules
import requests

target_url = "10.0.2.24/mutillidae/"

def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass	


with open("/home/faysal/Desktop/Coding/Python/subdomains.list", "r") as subdomains_list:
	for line in subdomains_list:
		word = line.strip()
		check_url = word + "." + target_url
		
		response = request(check_url)

		if response:
			print("[+] Discovered subdomain -->" + check_url)


with open("/home/faysal/Desktop/Coding/Python/common.txt", "r") as link_list:
	for line in link_list:
		word = line.strip()
		check_url = target_url + "/" + word		
		
		response = request(check_url)

		if response:
			print("[+] Discovered URL -->" + check_url)