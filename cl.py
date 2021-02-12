#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters, limit):
	#api takes a dict for filters and their values, including search query price etc
	# limit is needed but is not a key in the dict, rather, its used at a later step
	try:
		cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
		resp = cl_fs.get_results(sort_by='newest', limit=int(limit))
		results = [result['url'] for result in resp]
		if not results:
			print(f"\nNothing found for {filters['query']}")
			results = None
		return results
	except Exception as err:
		print("!"*20+"\t"+"!"*20+"\t")
		print(f"There was an error looking that up, please make sure field values are valid:\n\t{filters}")
		return None

def batchOpen(urls):
	if urls is None: return
	maxTabs = 5
	numberNewTabs = min(maxTabs, len(urls))
	show = input(f"Found {len(urls)} listings, open {numberNewTabs} in the browser?(y/n)\t")
	if show.lower() == 'n': return
	while show.lower() != 'q':
		for i in range(numberNewTabs):
				if not urls:
					show = 'q'
					break;
				os.system(f"open {urls.pop()}")
		remainingUrls = min(numberNewTabs,len(urls))
		if remainingUrls:
			show = input(f"Press any key to show {remainingUrls} more, press q to quit this search \t")
	print(f"Search Completed")

def promptForSearchParams(params={}):


	params['query'] = input("Search Term:  ") or None

	minprice = input("Min price: ") or None
	while minprice and not minprice.isdigit():
		minprice = input("Enter a valid number for Minimum Price  ")
	params['min_price'] = minprice

	maxprice = input("Max Price:  ") or None
	while maxprice and not maxprice.isdigit():
		maxprice = input("Enter a valid number for Maximum Price:  ")
	params['max_price'] = maxprice
	limit = input("Max Results To Show:  ") or None
	while limit and not limit.isdigit():
		limit = input("Enter a valid number for Max Results To Show:  ")
	params['posted_today'] = input("Only today\'s posts?)(y/n)\t").lower() == 'y'

	return limit, params

def splitArgs(args):
	# find the first non number from the end
	#partition the and recombine the list
	#assert(len(args) >= 2)
	i = -1
	while args[i].isdigit():
		i-=1
	i += 1
	if i == 0:
		return [" ".join(w for w in args)]
	return  [" ".join(w for w in args[:i])] + args[i:]

def main(args=None):
	fields = ['query', 'min_price', 'max_price', 'limit']
	while True:
		apiparams = {}
		limit = None
		#prompt if no args entered (first is the file name, count from 1 on)
		if not args:
			limit, apiparams=promptForSearchParams();
		else:
			#process args: combine and space delimt the strings (query) and leave number as tokens
			terms = splitArgs(args)

			#map args to fields
			apiparams = dict([x for x in zip(fields,splitArgs(args))])
			apiparams["posted_today"] = True
			if 'limit' in apiparams:
				limit = apiparams['limit']
				del apiparams['limit']
			#the args for subsequent searches (after current) must be prompted for (as opposed to entered as process argv) so clear args to trigger prompting
			args=None
		limit = 200 or limit
		urls = cl_search(apiparams, limit)
		batchOpen(urls)
		if input("To make another search type \"y \"\t ").lower() != "y":
			break
	quit()

if __name__ == "__main__":
	stars = "*"*60
	line = "-"*60
	cl = '{:^60}'.format("CRAIGSLIST CLI")
	print(stars)
	print(cl)
	print(stars)
	print(line)

	main(sys.argv[1:])

	print(line)
	print(stars)
	print(stars)
