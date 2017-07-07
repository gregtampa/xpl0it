#!/usr/bin/python
#proxy.py

#proxy module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import socks, socket

class proxy:
	
	def __init__(self, host, port, proxy_type):
		self.host = host
		self.port = port
		self.proxy_type = proxy_type
		
	def create_connection(self, address, timeout=None, source_address=None):
		self.sock = socks.socksocket()
		self.sock.connect(address)
		return self.sock
		
	def set_browser_proxy(self):
		try:
			socks.setdefaultproxy(self.proxy_type, self.host, int(self.port))
			socket.socket = socks.socksocket
			socket.create_connection = self.create_connection
			return True
		except:
			return False
		
	def set_socket_proxy(self):
		try:
			self.sock = socks.socksocket()
			self.sock.setproxy(self.proxy_type, self.host, int(self.port))
			return True
		except:
			return False
			
	def set_no_proxy(self):
		self.sock = socks.socksocket()
				
	def connect(self, host, port):
		try:
			self.sock.connect((host, port))
			return True 
		except:
			return False
	
	def send(self, datas):
		self.sock.send(str(datas))
		
	def recv(self, length):
		return self.sock.recv(length)
