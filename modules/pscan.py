#!/usr/bin/python
#pscan.py

#pscan module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3
  
import os, time
from socket import *

from auxilliary.proxy import *
from auxilliary.utils import *

class pscan():
	
	def __init__(self, args):
		self.target = args[1]
		self.proxy = args[2]
		self.proxy_type = args[3]
		self.verbose = args[4]
		self.results = ""
		
	def porttoservice(self, port): #common services
		
		if port == 21: return "Ftp"
		elif port == 22: return "Ssh"
		elif port == 23: return "Telnet"
		elif port == 25: return "Smtp"
		elif port == 80 or port == 8080: return "Http"
		elif port == 110: return "Pop3"
		elif port == 139: return "Netbios"
		elif port == 445: return "Smb"
		elif port == 1433: return "Microsoft SQL"
		elif port == 1521: return "Oracle SQL"
		elif port == 3306: return "MySQL"
		else: 
			return "Unknow"
		
	def scan(self):
		print "\n[+] Target: " + self.target
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
		
		if self.verbose == 1:
			print "[!] Scanning target...\n"
			
		for port in range(65535):
			try:
				if pr.connect(self.target, port) == True:
					pr.send("HEAD / HTTP/1.0\r\n\r\n")
					banner = pr.recv(1024)
					self.results += "%s/tcp open %s\n" %(port, self.porttoservice(port))
					print "[+] %s/tcp open %s" %(port, self.porttoservice(port))
					if banner != "":
						print banner
						self.results += banner + "\n"
			except:
				pass
			
		if self.results == "":
			self.results = "No open ports found"
			print "[-] Failed to connect to target"
			print "[-] " + self.results + "\n"
					
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "pscan_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> pscan report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Target: " + self.target + "\n")
		f.writelines("Results: \n\n" + self.results + "\n\n")

