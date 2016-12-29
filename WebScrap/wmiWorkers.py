#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import re

url="https://stafflist.wmi.amu.edu.pl/"

def scrap(url):
	response = urllib2.urlopen(url) 
	with open('wmiStaff.html','w') as f: f.write(response.read())

###################################################
with open('wmiStaff.html','r') as f: page_source = f.read()
soup = BeautifulSoup(page_source, 'html.parser')


table = soup.table
pattern = re.compile('^details/\d*')
links = []
for link in table.findAll('a'):
	string = link.get('href')
	if re.match(pattern,string):
		links.append(string)
###################################################
response = urllib2.urlopen(url+'details/1')
soup = BeautifulSoup(response.read(), 'html.parser')
soup = soup.body
soup.span.decompose()


degree = soup.h1.get_text()
name = soup.h2.get_text()
faculty = soup.h3.get_text().strip()

worker.append()

#.encode('utf-8')

print('{0} {1} {2}'.format(degree, name, faculty))
#print('{0} {1} {2}'.format(degree.encode('utf-8'), name.encode('utf-8'), faculty.encode('utf-8')))
