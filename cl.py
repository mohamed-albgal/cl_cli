#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters, lim):
	print(filters)
	cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
	resp = cl_fs.get_results(sort_by='newest', limit=lim)
	count = 0;
	results = []
	for result in resp:
		results.append(f"open {result['url']}")
		count+=1
	if count == 0:
		print(f"Nothing found for {filters['query']}")
		quit()
	show = input(f"Found {count} new listings, open each in a browser tab? (y/n)")
	if show.lower() == 'y' :
		for res in results:
			os.system(res)


argcount = len(sys.argv)
filters = {}
lim = 10


if argcount == 1:
	filters['query'] = input("Search Term: ")
	filters['min_price'] = input("Min price: ")
	filters['max_price'] = input("Max price: ")
	lim = input("Max Results To Show: ")
	lim = int(lim) if lim else 500
	filters['posted_today'] = False if input("Only today\'s posts?)(y/n)" ).lower() == 'n' else True
	cl_search(filters,lim);
	exit();
if argcount > 1:
	#query only
	filters['query'] = sys.argv[1]
	if argcount > 2:
		# query and minimum
		filters['min_price'] = sys.argv[2]
		if argcount > 3:
			# query min,max
			filters['max_price'] = sys.argv[3]
			if argcount > 4:
				#query, min, max, result limit
				lim = sys.argv[4]
filters["posted_today"] = True
lim = int(lim)
cl_search(filters,lim)



