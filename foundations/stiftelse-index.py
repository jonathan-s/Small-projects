#! /usr/bin/env python
# -*- coding: utf-8 -*- 

import urllib2
from bs4 import BeautifulSoup

register = open("stiftindex1.csv", "w")
x = 1000000
z = 1 
for y in range(40000):
	url = "http://www.stiftelser.lst.se/StiftWeb/FoundationDetails.aspx?id=" + str(x+y)
	f = urllib2.urlopen(url) 
	read = f.read()
	if not read[0] == "H":
		register.write(str(x+y)+", ")
		z = z + 1
		print z
	f.close()
