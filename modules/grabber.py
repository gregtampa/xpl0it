#!/usr/bin/python
#grabber.py

#grabber module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import os, time
from bs4 import BeautifulSoup

from auxilliary.proxy import *
from auxilliary.browser import *
from auxilliary.utils import *

class grabber:
	
	def __init__(self, args):
		self.target = check_url(args[1])
		self.proxy = args[2]
		self.proxy_type = args[3]
		self.verbose = args[4]
		self.results = ""
		
	def grab_links(self):
		print "\n[+] Target: " + self.target
		if self.verbose == 1:
			print "[!] Checking proxy..."
			
		if self.proxy != "":
			hst, prt = parse_address(self.proxy)
			pr = proxy(hst, prt, self.proxy_type)
			if pr.set_browser_proxy() == True:  
				print "[+] Proxy: " + self.proxy
			else:
				print "[-] Invalid or dead proxy"
		else:
			print "[-] Proxy not set"
				
		print
		
		if self.verbose == 1:
			print "[!] Connecting to target..."
		br = browser()
				
		try:
			site = br.open(self.target)
			src = site.read()
			soup = BeautifulSoup(src, "lxml")
			links = soup.find_all('a')
			
			if self.verbose == 1:
				print "[!] Found %d links\n" %(len(links))
			
			for link in links:
				print link.get("href")
		except:
			self.results = "No results found"
			print "[-] Failed to connect to target"
			print "[-] " + self.results + "\n"
					
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "grabber_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> grabber report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Target: " + self.target + "\n")
		f.writelines("Results:  \n\n" + self.results + "\n\n")
