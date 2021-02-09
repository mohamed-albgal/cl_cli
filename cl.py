#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters, lim):
	print(filters)
	try:
		lim = int(lim)
		cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
		resp = cl_fs.get_results(sort_by='newest', limit=lim)
		if not resp:
			raise Exception("There was an error scraping")
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
	except Exception:
		print(f"There was an error looking that up, please make sure field values are valid:\n\t{filters}")
		print(f"Limit entered was: {lim}")
		exitPrompt()

def exitPrompt():
	repeat = input("To make another search, type y\t")
	if repeat.lower() == "y":
		cleanStart()
	else:
		quit()

def batchOpen(opencommands):
	length = len(opencommands)
	numberNewTabs = 5 if length >= 5 else length
	show = input(f"Found {len(opencommands)} listings, open {numberNewTabs} in the browser?\t(y/n)")
	if show.lower() == 'n': exitPrompt()
	count = 0
	while show.lower() != 'q':
		for i in range(numberNewTabs):
				if not opencommands:
					exitPrompt()
					quit()
				os.system(opencommands.pop())
				count += 1
		left = numberNewTabs if numberNewTabs < length - count else length-count
		if left:
			show = input(f"Press any key to show {left} more, press q to quit\t")
		else:
			print(f"Finished")
			exitPrompt()
			quit()

def cleanStart():

	filters['query'] = input("Search Term: ") or None
	minp = input("Min price: ") or None
	filters['min_price'] = minp
	maxp =  input("Max price: ") or None
	filters['max_price'] = maxp
	lim = input("Max Results To Show: ") or 1000
	filters['posted_today'] = False if input("Only today\'s posts?)(y/n)" ).lower() == 'n' else True
	batchOpen(cl_search(filters,lim));

argcount = len(sys.argv)
filters = {}
lim = 1000

if argcount == 1:
	cleanStart();
else:
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
	batchOpen(cl_search(filters,lim))



