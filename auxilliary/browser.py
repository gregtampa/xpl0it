#!/usr/bin/python
#browser.py

#browser module for xpl0it v0.3
#Coded by wrh1d3 -> wrh1d3[at]gmail[dot]com
#Copyright (c) 2016-2017 J3kill Soft. by wrh1d3

import random
import mechanize, cookielib

user_agents = ['Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454101',
	'Mozilla/5.0 (Windows; U; Windows NT 6.0; de; rv:1.9.0.4) Gecko/2008102920 Firefox/3.0.1 (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; ch; rv:1.9.0.8) Gecko/2009032608 [www.VIS-Network.de]',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6',
    'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.9) Gecko/2009042115 Fedora/3.0.9-1.fc10 Firefox/3.0.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.9) Gecko/2009040821 Firefox/3.0.8 (de) (TL-FF) (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.0.9) Gecko/2009040821 Firefox/3.0.9',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.0.9) Gecko/2009040821 Firefox/3.0.4 (de) (TL-FF)',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.9) Gecko/2009040820 Firefox/3.0.9',
	'Mozilla/5.0 (compatible; Konqueror/3.1; Linux 2.4.22-10mdk; X11; i686; fr, fr_FR)',
	'Mozilla/5.0 (compatible; Konqueror/3.4; Linux) KHTML/3.4.2 (like Gecko)',
	'Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.15-1.2054_FC5; X11; i686; en_US) KHTML/3.5.4 (like Gecko)',
	'Mozilla/5.0 (compatible; Konqueror/3.5; Linux 2.6.16-2-k7) KHTML/3.5.0 (like Gecko) (Debian package 4:3.5.0-2bpo2)'
]

class browser(mechanize.Browser):
	
	def __init__(self):
		mechanize.Browser.__init__(self)
		self.set_handle_robots(False)
		self.set_handle_refresh(False)
		self.set_handle_equiv(True)  
		self.set_handle_redirect(True) 
		self.set_handle_referer(True) 
		self.set_handle_equiv(True)
		self.cookie = cookielib.LWPCookieJar()
		self.set_cookiejar(self.cookie)
		self.addheaders = [('User-agent', random.choice(user_agents))]
