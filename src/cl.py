#https://pypi.org/project/python-craigslist/
from cl_api.get_from_cl import search
import sys
from util.display import displayListings

def promptForSearchParams():
	params={}
	def validateInput(prompt):
		userinput = input(f"{prompt}: ") or None
		while userinput and not userinput.isdigit():
			userinput = input(f"Invalid input, re-enter {prompt}  ")
		return userinput
	params['query'] = input("\nSearch Term:  ") or None
	params['min_price'] = validateInput("Minimum Price")
	params['max_price'] = validateInput("Maximum Price")
	params['posted_today'] = input("Only today\'s posts?)(y/n)\t").lower() == 'y'
	return params

def parseArgs(args):
	apiparams = {}
	today=False
	# if last arg is a 'y' or 'n'
	if len(args[-1]) == 1 and args[-1].lower() == "y":
		today = True
		del args[-1]
	apiparams = dict(zip(['query', 'min_price', 'max_price'],args))
	apiparams['posted_today'] = today
	return apiparams

def main(args):
	while True:
		apiparams = promptForSearchParams() if not args else parseArgs(args)
		searchResults = search(apiparams) or print("Nothing found for {}".format(apiparams['query']))
		displayListings(searchResults)
		if args: break
		if "y" not in  input("\nPress 'y' to make another search:  ").lower(): break

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
	except Exception as e:
		#print(e)
		print("\n\n\n...there was an error please try again...\n\n\n")

	finally:
		print("\n",line)
