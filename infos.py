#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unicodecsv as csv
def getAll(surname):
	with open('wmiStaff.tsv') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	    	if surname in row['name'].lower():
	    		print('\n' + row['faculty'] + '\n\t'+ row['lvl'] + ' ' + row['name'] + '\n\ttelefon: ' + row['phone'] + '\n\te-mail: ' + row['mail'] + '\n\tpokoj: ' + row['room'] + '\n\tkonsultacje: ' + row['when'])

def search(value = 'gralinski',key = 'name',filters = ['faculty','position','lvl','name','room','phone','mail','website','when']):
	with open('wmiStaff.tsv') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	    	if value in row[key].lower():
	    		for reply in filters:
	    			print('\t' + reply + ': ' + row[reply])	
