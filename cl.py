#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys

def cl_search(filters):
	cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
	resp = cl_fs.get_results(sort_by='newest', limit=200)
	print(x for x in resp)
	urls = [x['url'] for x in resp]
	names= [x['name'] for x in resp]
	print(f"len of names: {len(names)}")
	print(f"len of urls: {len(urls)}")
	res = {}
	# for i in range(len(urls)): 
	# 	res[names[i]] = urls[i]
	# print(res)
	
	return None if not urls else res

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
	
	for i,x in enumerate(names):
		letter = chr(ord('a') + i)
		print(f"[{letter}]. {x}")
	choices = input("Enter the letter of the listing you want to view or type 'all' to show all")
	if choices.lower() == "all": 
		choices = [x for x in 'abcdefgh']
	for index in choices: 
		os.system("open {}".format(urls[ord(index)-ord('a')]))
		# print("f{}".format(urls[ord(index)-ord('a')]))

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
			searchResults = cl_search(searchResults)
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
	finally:
		print(line)
