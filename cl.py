#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters):
	try:
		cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
		resp = cl_fs.get_results(sort_by='newest', limit=200)
		results = [result['url'] for result in resp]
		return results or print(f"\n---Nothing found for {filters['query']}---\n")
	except:
		print("!"*20+"\t"+"!"*20+"\t")
		print(f"There was an external looking that up")
		return None

def batchOpen(urls):
	if urls is None: return
	maxTabs = 5
	numberNewTabs = min(maxTabs, len(urls))
	done = input(f"Found {len(urls)} listings, open {numberNewTabs} in the browser?(y/n)\t").lower() == 'n'
	while not done:
		for _ in range(numberNewTabs): 
			os.system(f"open {urls.pop()}")
		numberNewTabs = min(numberNewTabs,len(urls))
		done =  not numberNewTabs or input(f"Press any key to show {numberNewTabs} more, press q to quit this search \t").lower() == 'q'
	print(f"\n---Search Completed---\n")

def promptForSearchParams(params={}):
	
	def validateInput(prompt):
		userinput = input(f"{prompt}: ") or None
		while userinput and not userinput.isdigit():
			userinput = input(f"Invalid input, re-enter {prompt}  ")
		return userinput
	
	params['query'] = input("Search Term:  ") or None
	params['min_price'] = validateInput("Minimum Price")
	params['max_price'] = validateInput("Maximum Price")
	params['posted_today'] = input("Only today\'s posts?)(y/n)\t").lower() == 'y'
	return params

def splitArgs(args):
		words = list(filter(lambda x: type(x) is str, args))
		numbers = list(filter(lambda x: type(x) is int, args))
		return [" ".join(words)] + numbers

def main(args=None):
	fields = ['query', 'min_price', 'max_price']
	done = False
	while not done:
		#if no args, prompt for search parameters
		if not args:
			urls = cl_search(promptForSearchParams())
			batchOpen(urls)
			done = input("To make another search type \"y \"\t ").lower() != "y"
		else:
			userinputs = splitArgs(args)
			apiparams = dict([x for x in zip(fields,userinputs)])
			apiparams["posted_today"] = True
			urls = cl_search(apiparams)
			batchOpen(urls)
			break

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
