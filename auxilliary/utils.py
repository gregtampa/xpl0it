#!/usr/bin/python
#utils.py

#utils module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

def parse_address(address):
	addr = address.split(":")
	return addr[0], addr[1]

def check_url(url):
	if url[:7] != "http://":
		return "http://" + url
	elif url[:11] != "http://www.":
		return "http://www." + url

def check_proxy(address):		
	Result = True
		
	addr, prt = parse_address(address)
	if (addr == "") or (prt == ""): Result = False
	if int(prt) not in range(65535): Result = False
	
	ip = addr.split(".")
	if int(ip[0]) not in range(255): Result = False 
	if int(ip[1]) not in range(255): Result = False
	if int(ip[2]) not in range(255): Result = False 
	if int(ip[3]) not in range(255): Result = False
		
	return Result
