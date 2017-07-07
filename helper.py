#!/usr/bin/python
#helper.py

#helper module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

class helper:
	
	def __init__(self, module_name):
		self.module_name = module_name
		
	def print_help(self):
		if self.module_name == "":
			print "\nhelp\t\tPrint this help message"
			print "modules\t\tShow modules list"
			print "load\t\tLoad a module by name"
			print "bash\t\tRun bash command"
			print "exit\t\tExit program\n"
		else:
			if self.module_name == "gquery":
				print "\n[Usage]:\tload gquery [google query]"
				print "[Example]:\tload gquery index of pdf C programming\n"
			elif self.module_name == "grabber":
				print "\n[Usage]:\tload grabber [target]"
				print "[Example]:\tload grabber http://www.site.com/index.php\n"
			elif self.module_name == "vscan":
				print "\n[Usage]:\tload vscan [target]"
				print "[Example]:\tload vscan http://www.site.com\n"
			elif self.module_name == "pscan":
				print "\n[Usage]:\tload pscan [target]"
				print "[Example]:\tload pscan http://www.site.com\n"
			elif self.module_name == "fbcrack":
				print "\n[Usage]:\tload fbcrack [target email or phone]"
				print "[Example]:\tload fbcrack user@mail.com\n"
			elif self.module_name == "ftpcrack":
				print "\n[Usages]:\tload ftpcrack [username]"
				print "          \tload ftpcrack(for users list use)"
				print "[Examples]:\tload ftpcrack root"
				print "          \tload ftpcrack\n"
			elif self.module_name == "httpcrack":
				print "\n[Usage]:\tload httpcrack [username] [login form name] [password form name]"
				print "[Example]:\tload httpcrack root email pass or load httpcrack email pass (userslist use)\n"
			
	def print_modules(self): 
		print "\ngquery\t\tPerform a google search query"
		print "grabber\t\tExtract all links from a webpage"
		print "vscan\t\tCommon vulnerabilities scanner"
		print "pscan\t\tTcp port scanner and banner grabber"
		print "fbcrack\t\tFacebook password cracker"
		print "ftpcrack\tFTP password cracker"
		print "httpcrack\tHTTP password cracker\n\n"
		print "Type \"modules [module name]\" for more infos\n"
