#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters, lim):
	print(filters)
	cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
	resp = cl_fs.get_results(sort_by='newest', limit=lim)
	if not resp:
		print("failed to get a response from the scraping service")
	count = 0;
	results = []
	for result in resp:
		results.append(f"open {result['url']}")
		count+=1
	if count == 0:
		print(" ")
		print(f"Nothing found for {filters['query']}")
		exitPrompt();

	return results

def exitPrompt():
	repeat = input("To make another search, type y")
	if repeat.lower() == "y":
		cleanStart()
	else:
		quit()

def batchOpen(urls):
	length = len(urls)
	numberNewTabs = 5 if  length >= 5 else length
	show = input(f"Found {len(urls)} listings, open {length} in the browser?(y/n)")
	if show.lower() == 'n': quit()
	while show.lower() != 'q':
		for i in range(numberNewTabs):
				if (i < length):
					os.system(results.pop())
				else:
					print("No more to show")
					exitPrompt()
		show = input(f"Press any key to show more, pres q to quit")

def cleanStart():
	filters['query'] = input("Search Term: ")
	filters['min_price'] = input("Min price: ")
	filters['max_price'] = input("Max price: ")
	lim = input("Max Results To Show: ")
	lim = int(lim) if lim else 500
	filters['posted_today'] = False if input("Only today\'s posts?)(y/n)" ).lower() == 'n' else True
	batchOpen(cl_search(filters,lim));

argcount = len(sys.argv)
filters = {}
lim = 10

if argcount == 1:
	cleanStart();
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
batchOpen(cl_search(filters,lim))



