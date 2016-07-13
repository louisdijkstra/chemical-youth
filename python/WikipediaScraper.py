import os
import sys
import numpy as np
import urllib3
import time
import json
from bs4 import BeautifulSoup
import requests
import shutil

"""
	File containing helper functions for crawling
	Wikipedia articles, revisions, references etc.
"""


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


def get_old_ids(title): 
	""" 
		Returns all the old ids of a particular site given the title of the 
		Wikipedia page
	"""
	raw_data = json.loads( readInDataFromURL("https://en.wikipedia.org/w/api.php?action=query&prop=revisions&format=json&rvlimit=100000&titles=" + title) )
	
	old_ids = dict() # initialize 

	for page_id, revisions in data['query']['pages'].items(): 
		print(revisions)
		# for revision in revisions: 
		# 	old_ids[revision.]	

		# 	try: 
		# 		for extlink in page['extlinks']: 
		# 			# print to the output file
		# 			print('%s\t%s\t%s'%(page_id, name, extlink['*']), file=outputfile)
		# 	except: 
		# 		if options.verbose: 
		# 			print('Page %s does not have any external links...'%name)		


	# print(data)

	return old_ids


def get_links(linkfile, api_command = ''): 
	"""
		Gets the links in the given file. Returns all the links
		in a list. 
	"""
	names, links = [], [] 

	for line in linkfile: 
		names.append( line.strip() )
		links.append( api_command + line.strip() )

	return names, links