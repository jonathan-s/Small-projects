# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
import sys
import urllib2

reload(sys).setdefaultencoding('utf8')

#Code for making headlines.
def makeheadlines():
	#include html for making headlines. You have to open some html some way and make beautiful soup. 
	f = urllib2.urlopen("http://www.stiftelser.lst.se/StiftWeb/FoundationDetails.aspx?id=1020991")
	html = f.read()
	soup = BeautifulSoup(html) #soup obj
	td = soup.find_all('td')
	x = 1
	for x in xrange(1, len(td), 2):
		stiftwr.write(td[x].get_text() + "# ")
	stiftwr.write("\n")
	return

def extract(soup): #extracts content from html and writes it to file. 
	soup = BeautifulSoup(html) #turns it into a soup object. 
	td = soup.find_all('td')
	for x in xrange(2, len(td), 2):
		#print td[x].get_text()
		stiftwr.write(td[x].get_text() + "# ")
	stiftwr.write("\n")
	return 

def stiftindex():
	nrlist = []
	nr = ''
	f = open("stiftindex1.csv") #open the right file. 
	stift = f.read()
	for x in range(len(stift)):
		nr = nr + stift[x]
		if stift[x] == ',':
			nrlist.append(nr[1:len(nr)-1]) #removes first blankspace and comma. 
			nr = ''
		#print x
	return nrlist

#main application

stiftwr = codecs.open("stiftelse_out.csv", "w", "utf8")
index = stiftindex()

makeheadlines()
for x in range(len(index)):
	f = urllib2.urlopen("http://www.stiftelser.lst.se/StiftWeb/FoundationDetails.aspx?id=" + index[x])
	html = f.read()
	extract(html) #function for extracting content
	print x
	f.close()



