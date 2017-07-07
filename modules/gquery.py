#!/usr/bin/python
#gquery.py

#gquery module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import os, urlparse, time
from bs4 import BeautifulSoup

from auxilliary.proxy import *
from auxilliary.browser import *
from auxilliary.utils import *

class gquery:
	
	def __init__(self, args): 
		self.query = ""
		for q in args[1]:
			self.query += q + " "
		self.home_page = "https://www.google.com"
		self.proxy = args[2]
		self.proxy_type = args[3]
		self.verbose = args[4]
		self.results = ""
			
	def search_query(self):
		print ("\n[+] Query: " + self.query)
		if self.verbose == 1:
			print ("[!] Checking proxy...")
			
		if self.proxy != "":
			hst, prt = parse_address(self.proxy)
			pr = proxy(hst, prt, self.proxy_type)
			if pr.set_browser_proxy() == True:  
				print ("[+] Proxy: " + self.proxy)
			else:
				print ("[-] Invalid or dead proxy")
		else:
			print ("[-] Proxy not set"
				
		print
		
		if self.verbose == 1:
			print ("[!] Connecting to google...\n")
		br = browser()
				
		try:
			br.open(self.home_page)
			br.select_form(nr=0)
			br['q'] = '%s' %(self.query)
			resp = br.submit()
			src = resp.read()
			soup = BeautifulSoup(src, "lxml")
				
			if self.verbose == 1:
				print ("[!] Query search results\n")
			
			for link in soup.select('.r a'):
				res = urlparse.parse_qs(urlparse.urlparse(link['href']).query)['q'][0]
				self.results += res + "\n"
				print (res)
		except:
			self.results = "No results found"
			print ("[-] Failed to connect to google")
			print ("[-] " + self.results + "\n")
				
	def generate_report(self):
		date = time.strftime("%d-%m-%Y")
		filename = "gquery_report_%s.txt" %(date)
		
		if not os.path.exists(os.getcwd() + "/reports/" + filename): 
			f = open(os.getcwd() + "/reports/" + filename, "w")
			f.writelines("[!] xpl0it penetration testing toolkit -> gquery report\n\n")
			
		f = open(os.getcwd() + "/reports/" + filename, "a")
		f.writelines("Query: " + self.query + "\n")
		f.writelines("Results: \n\n" + self.results + "\n\n")
