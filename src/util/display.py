import os

def batchShow(listings, count,totalcount):
	records = dict(zip([x for x in "abcdefgh"],listings))
	# records are "a" --> { url: .., name:..., price:..., location:...} ...
	while records:
		print(f"\n-----Page {count} of {totalcount}-----\n")
		for letter in records:
			print(f"[{letter}]--{records[letter]['price'].strip()}--{records[letter]['name'].strip()}")
		choices = input("\n\nEnter the letter(s) of the listing(s) or 'all' or 'q' to quit: ").lower()
		if choices == "q": return False
		if not choices: break
		#ignore invalid choices with filtter (duplicates and random letters)
		choices = set(filter(lambda e: e in records.keys(), [x for x in choices])) if choices != "all" else records.keys()
		urls = " ".join([records[letter]['url'] for letter in choices])
		os.system(f"open {urls}")
		newKeys = set(records.keys()).symmetric_difference(choices)
		records = {x : records[x] for x in records.keys() if x in newKeys }
	return True

def interactiveListings(listings, batchSize=8):
        if not listings: return
        i=0
        count=1
        resume=True
        total=(len(listings) // batchSize)
        total=total + 1 if len(listings) % batchSize > 0 else total
        print(f"\nFound {len(listings)} listings")
        while i < len(listings) and resume:
                resume = batchShow(listings[i : i+batchSize], count, total)
                i += batchSize
                count += 1

