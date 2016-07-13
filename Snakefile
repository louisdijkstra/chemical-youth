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


rule classify_users: 
	input:   'data/users-designer-drugs.tsv'
	output:  'data/unique-users-designer-drugs.tsv'
	message: 'Creating a list of all unique users, classifying them as bots or anonymized users. Output is stored at {output}.'
	shell:   'python bin/get-unique-users.py --add-columns {input} > {output}'

# scrape the users that revised the articles on designer drugs
rule scrape_users:
	output:		'data/users-designer-drugs.tsv'		
	message:	'Scraping the users for the designer drugs. The raw data is stored @ {output}.'
	shell: 		'python bin/scrape-users.py -v data/list-designer-drugs.txt {output}'


# scrape the external links from the designer drugs pages
rule scrape_external:
	output:		'data/external-links-designer-drugs.tsv'		
	message:	'Scraping the external links for the designer drugs. The raw data is stored @ {output}.'
	shell: 		'python bin/scrape-external-links.py --sleep 1 -v data/list-designer-drugs.txt {output}'
