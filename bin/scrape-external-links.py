#!/usr/bin/env python
from __future__ import print_function, division
from optparse import OptionParser
import os
import sys
import numpy as np
import urllib3
import time
import json
from bs4 import BeautifulSoup
import requests
import shutil

# add the python directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__))[:-3] + 'python')

__author__ = "Louis Dijkstra"

usage = """%prog <title> <output.csv>

	<title>			title of the wikipedia page to be crawled or a 
					file with a list of titles (every row a different
					title)
	<output.csv> 	output file location

Scraps the external links of all Wikipedia pages in the 
<link-list.txt> file. The output is stored in CSV format 
(tab-delimited). It contains the following columns: 
"""

API_LINE = "https://en.wikipedia.org/w/api.php?action=query&prop=extlinks&format=json&ellimit=5000&titles="

def get_links(linkfile): 
	"""
		Gets the links in the given file. Returns all the links
		in a list. 
	"""
	names, links = [], [] 

	for line in linkfile: 
		names.append( line.strip() )
		links.append( API_LINE + line.strip() )

	return names, links

def readInDataFromURL(site): 
	"""
		Reads in the html data from a given site

		Args: 
			site - site location (string)

		Returns:
			text
	"""
	http    = urllib3.PoolManager()
	request = http.request('GET', site)  # get the data
	soup    = BeautifulSoup(request.data)
	return soup.get_text()

def printHeader(file): 
	print("page_id\tname\texternal_link", file=file)

def main():

	parser = OptionParser(usage=usage)	
	parser.add_option("--sleep", "-s", action="store", dest="sleep", default=None, type=float, 
				  			help="Sleep time scraping two pages. (Default: no sleep)")
	parser.add_option("-v", action="store_true", dest="verbose", default=False, 
				  			help="verbose.")
	(options, args) = parser.parse_args()
	
	# process arguments
	if (len(args)!=2):
		parser.print_help()
		return 1

	try: 
		linkfile = open(args[0], 'r')
		names, links = get_links(linkfile)
	except: 
		names, links = [args[0]], [API_LINE + args[0]]

	outputfilename = args[1] 

	print(names)
	print(links)

	i       = 0
	n_links = len(links)

	outputfile = open(outputfilename, 'w')

	printHeader(outputfile)

	# go through all the wikipedia links
	for name, link in zip(names, links): 

		if options.verbose: 
			i += 1
			print('%d of %d links processed... (%.2f %%)'%(i, n_links, float(i) / float(n_links) * 100))

		# get the raw data
		data = json.loads(readInDataFromURL(link))

		# walk through the external links
		for page_id, page in data['query']['pages'].items(): 
			try: 
				for extlink in page['extlinks']: 
					# print to the output file
					print('%s\t%s\t%s'%(page_id, name, extlink['*']), file=outputfile)
			except: 
				if options.verbose: 
					print('Page %s does not have any external links...'%name)		

		if options.sleep != None: 
			time.sleep(options.sleep)

	if options.verbose: 
		print(" DONE")
	
if __name__ == '__main__':
	sys.exit(main())