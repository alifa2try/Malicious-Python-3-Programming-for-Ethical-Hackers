#!/usr/bin/env python3

# This program crawls websites


# import modules
import argparse
import requests
import re
import urllib.parse


def get_argument():
	parser = argparse.ArgumentParser()
	parser.add_argument("domain", help="Domain to search email from")
	option = parser.parse_args()

	if not option.domain:
		parser.error("[-] You need to specify a domain to search emails from")

	return option.domain	


def get_links_from_url(url):
	try:
		response = requests.get(url)
		return re.findall('(?:href=")(.*?)"', (response.content).decode())
	except UnicodeDecodeError:
		pass	
	

def extract_mails(url):
	try:
		response = requests.get(url)
		return re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', (response.content).decode())
	except UnicodeDecodeError:
		pass		


def crawl_links(url):
	try:
		links = get_links_from_url(url)

		for link in links:
			link = urllib.parse.urljoin(url, link)
			
			if '#' in link:
				link = link.split('#')[0]
				

			if target_url in link and link not in link_list:
				link_list.append(link)

				mails = extract_mails(link)

				for mail in mails:
					if mail not in mail_list:
						mail_list.append(mail)
						print(f"[+] Found an e-mail >> {mail}")
				crawl_links(link)
	except TypeError:
		pass			

try:
	mail_list = []
	link_list = []
	domain = get_argument()
	target_url = "https://" + domain
	crawl_links(target_url)
except KeyboardInterrupt:
	print("[+] Detected CTRL + C and the program will now halt!")