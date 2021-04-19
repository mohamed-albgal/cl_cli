#https://pypi.org/project/python-craigslist/
from cl_api.get_from_cl import search
import sys
from util.display import interactiveListings


def promptForSearchParams():
	params={}
	def validateInput(prompt):
		userinput = input(f"{prompt}: ") or None
		while userinput and not userinput.isdigit():
			userinput = input(f"Invalid input, re-enter {prompt}:   ")
		return userinput
	params['query'] = input("\nSearch Term:  ") or None
	params['min_price'] = validateInput("Minimum Price")
	params['max_price'] = validateInput("Maximum Price")
	params['posted_today'] = input("Only today\'s posts?)(y/n)\t").lower() == 'y'
	return params

def zipArgs(args):
	apiparams = {}
	today=False
	# see if last argument is a 'y'
	today = len(args[-1]) == 1 and args[-1].lower() == "y"
	apiparams = dict(zip(['query', 'min_price', 'max_price'],args))
	apiparams['posted_today'] = today
	return apiparams

def showListingsNonInteractive(args):
    try:
        listings = search(zipArgs(args))
        if not listings: return
        print(f"Query: {listings[0]['query']}\n")
        for i in range(len(listings)):
            print("[{}]---{}--{}--{}\n{}".format(i,listings[i]['price'], listings[i]['name'],listings[i]['location'], listings[i]['url']))
        print('\n')
    except Exception as e:
        raise Exception


def printbanner():
	stars = "*"*60;line = "-"*60;cl = '{:^60}'.format("CRAIGSLIST CLI")
	print(stars);print(cl);print(stars);print(line)

def main(args):
        try:
            if args and args[0] == 'script':
                    showListingsNonInteractive(args[1:])
                    return
            printbanner()
            while True:
                    apiparams = promptForSearchParams() if not args else zipArgs(args)
                    searchResults = search(apiparams) or print(f"Nothing found for {  apiparams['query']  }")
                    interactiveListings(searchResults)
                    if  args or "y" not in  input("\nPress 'y' to make another search:  ").lower(): break
            print("-"*60)
        except Exception as e:
            raise Exception

if __name__ == "__main__":
	try:
		main(sys.argv[1:])
	except SystemExit:
		pass
	except KeyboardInterrupt:
		pass
	except Exception as e:
		#print(e)
		print("\n\n\n...there was an error please try again...\n\n\n")
