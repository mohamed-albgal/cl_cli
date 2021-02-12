#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters, limit):
	#api takes an dict for filters and their values, including search query price etc
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
		print(err)
		print(f"There was an error looking that up, please make sure field values are valid:\n\t{filters}")
		return None

def batchOpen(urls):
	if urls is None: return
	length = len(urls)
	numberNewTabs = 5 if length >= 5 else length
	show = input(f"Found {len(urls)} listings, open {numberNewTabs} in the browser?\t(y/n)")
	if show.lower() == 'n': return
	count = 0
	while show.lower() != 'q':
		for i in range(numberNewTabs):
				if not urls:
					show = 'q'
					break;
				os.system(f"open {urls.pop()}")
				count += 1
		moreleft = numberNewTabs if numberNewTabs < length - count else length-count
		if moreleft:
			show = input(f"Press any key to show {moreleft} more, press q to quit this search \t")
	print(f"Search Completed")

def promptForSearchParams(params={}):
	params['query'] = input("Search Term: ") or None
	params['min_price'] = input("Min price: ") or None
	params['max_price'] = input("Max price: ") or None
	limit = input("Max Results To Show: ") or None
	params['posted_today'] = False if input("Only today\'s posts?)(y/n)\t").lower() == 'n' else True

	return limit, params


def main(args=[None]):

	queryModifiers = ['query', 'min_price', 'max_price', 'limit']
	while True:
		argcount = len(args)
		apiparams = {}
		limit = None
			#buggy, enclosed string still counted as many tokens instead of one
		if argcount == 1:
			limit, apiparams=promptForSearchParams();
		else:
			apiparams = dict([x for x in zip(queryModifiers,args[1:])])
			apiparams["posted_today"] = True
			if 'limit' in apiparams:
				limit = apiparams['limit']
				del apiparams['limit']
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

	main(sys.argv)

	print(line)
	print(stars)
	print(stars)
