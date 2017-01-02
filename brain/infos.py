#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unicodecsv as csv

with open('wmiStaff.tsv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	#if 'Żuro' in row['name'].split()[1]:
    	print(row['name'] + ' ' + row['mail'])
