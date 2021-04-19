
def search(filters):
    try:
        
        from craigslist import CraigslistForSale
        clobject = CraigslistForSale(site='sfbay', area='', category='sss', filters=filters)
        response = clobject.get_results(sort_by='newest', limit=500)
        return None if not response else [{"query":filters["query"], "name":item['name'], "url":item['url'], "price":item['price'], "location": item['where']} for item in response]
    except:
        raise Exception
