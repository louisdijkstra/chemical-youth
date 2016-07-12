import os 
import os.path
import sys
import subprocess
import snakemake.utils

___author___ = "Louis Dijkstra"

# rule all: 
# 	input: 		'data/ecstasy_color.csv'
# 	output: 	'data/ecstasy.csv'
# 	message: 	'Collecting and preprocessing the data'
# 	shell: 		'cp {input} {output}'

"""
	COLLECTING AND PREPROCESSING THE DATA
"""

# scrape the external links from the designer drugs pages
rule scrape:
	output:		'data/external-links-designer-drugs.tsv'		
	message:	'Scraping the external links for the designer drugs. The raw data is stored @ {output}.'
	shell: 		'python bin/scrape-external-links.py --sleep 1 -v data/list-designer-drugs.txt {output}'
