#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters):
	cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
	resp = cl_fs.get_results(sort_by='newest', limit=200)
	res = {}
	for x in resp:
		res[x['name']]=x['url']
	return res or None

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

def batchShow(names,urls):
	done = ""
	letters = [x for x in 'abcdefgh']
	while done != "next" and urls: 
		for i,x in enumerate(names): 
			print(f"[{letters[i]}]. {x}")
		choices = input("Enter the letter of the listing you want to view or type 'all' to show all\t")
		if choices.lower() == "all": 
			choices = [x for x in 'abcdefgh']
		else: 
			choices = list(filter(lambda x: x in letters, choices))
		for index in choices:
			choice = ord(index)-ord('a')
			os.system("open {}".format(urls[choice]))
			del names[choice]
			del urls[choice]
			del letters[choice]
		done = input("To show next batch enter 'next' or continue")

def displayListings(listings):
	if not listings:
		print(f"\n---Nothing found---\n")
		return
	index = 0
	count = len(listings)
	names=[x for x in listings.keys()]
	urls = [x for x in listings.values()]
	while index < count:
		batchShow(names[index:index+8], urls[index:index+8])
		index += 8

def main(args=None):
	fields = ['query', 'min_price', 'max_price']
	done = False
	while not done:
		#if no args, prompt for search parameters
		if not args:
			searchResults = cl_search(promptForSearchParams())
			displayListings(searchResults)
			done = input("To make another search type \"y \"\t ").lower() != "y"
		else:
			userinputs = splitArgs(args)
			apiparams = dict([x for x in zip(fields,userinputs)])
			apiparams["posted_today"] = True
			searchResults = cl_search(apiparams)
			displayListings(searchResults)
			break

if __name__ == "__main__":
	stars = "*"*60
	line = "-"*60
	cl = '{:^60}'.format("CRAIGSLIST CLI")
	print(stars)
	print(cl)
	print(stars)
	print(line)
	try:
		main(sys.argv[1:])
	except SystemExit:
		pass
	except KeyboardInterrupt:
		pass
	finally:
		print(line)
