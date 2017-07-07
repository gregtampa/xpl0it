#!/usr/bin/python
#xpl0it.py v0.3

#xpl0it Penetration Testing Toolkit Framework 0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com / wrh1d3[at]xmpp[dot].jp
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

#-----#
#Inspired on Inguma Penetration Testing Toolkit 0.0.8 by Joxean Koret
#-----#

import sys, os
import readline, atexit

from helper import *

from modules.gquery import *
from modules.grabber import *
from modules.vscan import *
from modules.pscan import *
from modules.fbcrack import *
from modules.ftpcrack import *
from modules.httpcrack import *

from auxilliary.utils import *

banner = """ 
\t================================================                      
\t    _       _        _    _____                                       
\t   / |  __ / | _  _ / |  /    _\_   __   _                         
\t _ | | / _\| |/ |/ || |   \  / / \ /  \ / |                           
\t/ \| || __/|   < | || |  _/  \| - ||  > | _>                          
\t\___/  \__/|_/\_||_||_| /____/ \_/ | /  |__\O                       
\t                                                                      
\t                                    PRESENTS                          
\t                                                                      
\t================================================                      
\txpl0it Penetration Testing Toolkit Framework 0.3                          
\tCoded by wrh1d3 -> wrh1d3[at]gmail[dot]com  
\t  
\tCopyright (c) 2016-2017 J3kill Soft. by wrh1d3                          
\t================================================                      
\t                 __       ___       _  ___                           
\t___  _  __  ____ | |___  /  |    __| |/__  \                          
\t\  \/ \/  / | __\|  _  \  | |   / _  |   / /                          
\t \  ___  /  | |  | | | | _| |_ | /_| | __\ \                          
\t  \/   \/   |_|  |_| |_| |___| \_____|\____/                          
\t                                                                     
\tw r h 1 d 3 [ a t ] g m a i l [ d o t ] c o m                         
\t                                                                      
\t================================================                      
"""

global proxy_address
global proxy_type
global verbose_mode

proxy_address = ""
proxy_type = 2
verbose_mode = 0

modules_list = ["gquery", "grabber", "vscan", "pscan", "fbcrack", "ftpcrack", "httpcrack"]
commands_list = ["help", "bash", "load", "modules"]

def print_usage():
	print (banner)
	print ("\nUsage: python ./xpl0it.py [Options]")
	print ("\n[Options]")
	print ("  -h, --help\tPrint this help message")
	print ("  -v VERBOSE\tSet verbose mode")
	print ("  -p PROXY\tSet proxy address (host:port)")
	print ("    --http\tHttp proxy type")
	print ("    --socks4\tSocks4 proxy type")
	print ("    --socks5\tSocks5 proxy type")
	print ("\n[Example]")
	print ("  python ./xpl0it.py -v -p 127.0.0.1:9050 --socks5\n") #Tor proxy
		
def setup_prompt():
	hf = os.path.expanduser("__history__")
	if os.path.exists(hf) == True: 
		readline.read_history_file(hf)
	atexit.register(readline.write_history_file, hf)
		
def bash_execute(args):
	cmd = ""
	for arg in args[1:len(args)]: 
		cmd += arg + " "
	os.system(cmd)

def load_module(module_name, args):
	if not module_name in modules_list:
		print ("\n[-] Unknown module '%s'" %(module_name))
		print ("[!] Type \"modules\" for modules list\n")
	else:
		if module_name == "gquery":
			if len(args[1:len(args)]) < 2: 
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2:], proxy_address, proxy_type, verbose_mode)
				gq = gquery(args_tuple)
				gq.search_query()
				gq.generate_report()
		elif module_name == "grabber":
			if len(args[1:len(args)]) < 2: 
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2], proxy_address, proxy_type, verbose_mode)
				gb = grabber(args_tuple)
				gb.grab_links()
				gb.generate_report()
		elif module_name == "pscan":
			if len(args[1:len(args)]) < 2: 
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2], proxy_address, proxy_type, verbose_mode)
				ps = pscan(args_tuple)
				ps.scan()
				ps.generate_report()
		elif module_name == "fbcrack":
			if len(args[1:len(args)]) < 2:
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2], proxy_address, proxy_type, verbose_mode)
				fb = fbcrack(args_tuple)
				fb.crack()
				fb.generate_report()
		elif module_name == "ftpcrack":
			if len(args[1:len(args)]) < 3: 
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2], args[3], proxy_address, proxy_type, verbose_mode)
				ftp = ftpcrack(args_tuple)
				ftp.crack()
				ftp.generate_report()
		elif module_name == "httpcrack":
			if len(args[1:len(args)]) < 5: 
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2], args[3], args[4], args[5], proxy_address, proxy_type, verbose_mode)
				http = httpcrack(args_tuple)
				http.crack()
				http.generate_report()
		else:
			if len(args[1:len(args)]) < 2: 
				print ("\n[-] Not enough arguments")
				print ("[!] Type \"modules %s\" for more infos\n" %(module_name))
			else:
				args_tuple = (None, args[2], proxy_address, proxy_type, verbose_mode)
				vs = vscan(args_tuple)
				vs.scan()
				vs.generate_report()

def check_commands(cmds):
	cmd = cmds.split(" ")
	 
	if not cmd[0] in commands_list:
		print ("\n[-] Unknown command '%s'" %(cmd[0]))
		print ("[!] Type \"help\" for commands list\n")
	else:
		if cmd[0] == "help": 
			hlp = helper("")
			hlp.print_help()
		elif cmd[0] == "bash":
			if len(cmd) < 2: 
				print ("\n[-] Not enough arguments") 
				print ("[!] Usage: bash [command]\n")
			else: 
				bash_execute(cmd)
		elif cmd[0] == "load":
			if len(cmd) - 1 < 2: 
				print ("\n[-] Not enough arguments")
				print ("[!] Usage: load [module name] [arguments]")
				print ("[!] Type \"modules\" for modules list\n")
			else: 
				load_module(cmd[1], cmd)
		else:
			if len(cmd) == 1: 
				hlp = helper("")
				hlp.print_modules() 
			else:
				if not cmd[1] in modules_list:
					print ("\n[-] Unknown module '%s'" %(cmd[1]))
					print ("[!] Type \"modules\" for modules list\n")
				else:
					hlp = helper(cmd[1])
					hlp.print_help() 
		
def main_loop():
	while True:
		user_input = raw_input("xpl0it_framewrok> ")
		if user_input == "exit":
			break
		else: 
			check_commands(user_input)

#by wrh1d3
#-----
def get_argv_bool(opt):
	Result = False
	for arg in range(len(sys.argv)):
		if ("-" in sys.argv[arg]) and (opt in sys.argv[arg]):
			Result = True
	return Result
	
def get_argv_str(opt):
	Result = "" 
	for arg in range(len(sys.argv)):
		if sys.argv[arg] == opt:
			Result = sys.argv[arg + 1]
	return Result
#-----
	
def main():
	global proxy_address
	global proxy_type
	global verbose_mode
	
	if (get_argv_bool("-h") == True) or (get_argv_bool("-help") == True):
		print_usage()
		sys.exit(1)
		
	if get_argv_bool("-v"):
		verbose_mode = 1
		
	proxy_address = get_argv_str("-p")
	
	if proxy_address != "":
		if check_proxy(proxy_address) == False:
			print ("[-] Invalid proxy address")
			sys.exit(1)
	
	if get_argv_bool("-http") == True:
		proxy_type = 3
	elif get_argv_bool("-socks4") == True:
		proxy_type = 1
	elif get_argv_bool("-socks5") == True:
		proxy_type = 2
		
	setup_prompt()
	print (banner) 
	main_loop()
	
if __name__ == '__main__':
	main()
