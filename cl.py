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

ac = len(sys.argv)
filters = {}
lim = 10
if ac == 1 :
	filters['query'] = input("Search Term: ")
	filters['max_price'] = input("Enter max price: ")
	filters['min_price'] = input("Enter min price: ")
	lim = input("Enter max listings to open: ")
	lim = int(lim) if lim else 500
	filters['posted_today'] = False if input("Only today\'s posts?)(y/n)" ).lower() == 'n' else True
	cl_search(filters,lim);
	exit();

if ac > 1:
	#query only
	filters['query'] = sys.argv[1]
	if ac > 2:
		# query and lim
		filters['min_price'] = sys.argv[2]
		if ac > 3:
			# query and lim and max
			filters['max_price'] = sys.argv[3]
			if ac > 4:
				#query and lim and max and min
				lim = sys.argv[4]
filters["posted_today"] = True
lim = int(lim)
cl_search(filters,lim)



