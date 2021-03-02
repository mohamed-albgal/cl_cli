#https://pypi.org/project/python-craigslist/
from craigslist import CraigslistForSale
import os
import sys
import math

def cl_search(filters):
	cl_fs = CraigslistForSale(site='sfbay', area='sby', category='sss',filters=filters)
	resp = cl_fs.get_results(sort_by='newest', limit=200)
	res = {}
	for x in resp: 
		item=[x['url'], x['price'], x['where']]
		res[x['name']]=item
	return res or None

def promptForSearchParams(params={}):
    	
	def validateInput(prompt):
		userinput = input(f"{prompt}: ") or None
		while userinput and not userinput.isdigit():
			userinput = input(f"Invalid input, re-enter {prompt}  ")
		return userinput
	
	params['query'] = input("\n\nSearch Term:  ") or None
	params['min_price'] = validateInput("Minimum Price")
	params['max_price'] = validateInput("Maximum Price")
	params['posted_today'] = input("Only today\'s posts?)(y/n)\t").lower() == 'y'
	return params

def splitArgs(args): 
	words = list(filter(lambda x: type(x) is str, args))
	numbers = list(filter(lambda x: type(x) is int, args))
	return [" ".join(words)] + numbers

def batchShow(listings, count,totalcount):
	records = dict(zip([x for x in "abcdefgh"],listings))
	while records: 
		#show the titles
		print(f"\n-----Page {count} of {totalcount}-----\n")
		for letter in records: 
			tup = records.get(letter)
			price = tup[1][1]
			#location = tup[1][2]
			print(f"[{letter}]--{price}--{tup[0].strip()}")
		choices = input("\n\nEnter the letter(s) of the listing(s) or 'next' or 'all:' ").lower()
		if choices == "next": break
		choices = set(filter(lambda e: e in records.keys(), [x for x in choices])) if choices != "all" else [x for x in records.keys()]
		for letter in choices:
			os.system(f"open {records.get(letter)[1][0]}")
			del records[letter]
			

def displayListings(query,listings, batchSize=8):
	if not listings:
		print(f"\n---Nothing found for {query}---\n")
		return
	i = 0;
	count = 1
	items = list(listings.items())
	total = math.ceil(len(items) / batchSize) 
	print(f"\nFound {len(listings)} listings")
	while i < len(items):
		batchShow(items[i:i+batchSize], count, total)
		i+=batchSize
		count += 1


def main(args=None):
	fields = ['query', 'min_price', 'max_price']
	done = False
	while not done:
		# if called without args, prompt
		if not args:
			inputs = promptForSearchParams()
			searchResults = cl_search(inputs)
			displayListings(inputs[0],searchResults)
			done = "y" not in  input("To make another search type \"y \"\t ").lower()
		else:
			userinputs = splitArgs(args)
			apiparams = dict([x for x in zip(fields,userinputs)])
			apiparams["posted_today"] = True
			searchResults = cl_search(apiparams)
			displayListings(apiparams['query'],searchResults,4)
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
		print("\n",line)
