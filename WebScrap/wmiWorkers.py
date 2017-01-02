#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib2, re
import unicodecsv as csv
from bs4 import BeautifulSoup


url="https://stafflist.wmi.amu.edu.pl/"

def scrap(url):
	response = urllib2.urlopen(url) 
	with open('wmiStaff.html','w') as f: f.write(response.read())


def getStaff():
	with open('wmiStaff.html','r') as f: page_source = f.read()
	soup = BeautifulSoup(page_source, 'html.parser')


	table = soup.table
	pattern = re.compile('^details/\d*')
	links = []
	for link in table.findAll('a'):
		string = link.get('href')
		if re.match(pattern,string):
			links.append(string)
	return links


def getInfo(sublink):
	response = urllib2.urlopen(url+sublink)
	soup = BeautifulSoup(response.read(), 'html.parser')
	soup = soup.body
	#soup.span.decompose()


	degree = soup.h1.get_text()
	name = soup.h2.get_text()
	faculty = soup.h3.get_text().strip()
	info = {}
	for tr in soup.table.findAll('tr'):
		info[tr.th.get_text().encode('utf-8')] = tr.td.get_text().encode('utf-8')

	lvl = info['stopień naukowy']
	position = info['stanowisko']
	room = info['pokój']
	phone = info['telefon']
	mail = info['e-mail']
	if 'dyżury' in info.keys():
		when = "".join(info['dyżury'].split())
	else:
		when = 'No'

	return {'name':name, 'degree':degree, 'faculty':faculty,'lvl':lvl, 'position':position, 'room':room,'phone':phone, 'mail':mail, 'when':when}


with open('wmiStaff.tsv', 'a') as csvfile:
	fieldnames = ['name', 'degree', 'faculty','lvl', 'position', 'room','phone' ,'mail', 'when']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for i in getStaff():
		print i
		writer.writerow(getInfo(i))





