from typing import Text
import cl
import unittest

class TestSuite(unittest.TestCase):
    keys = ['query', 'max_price', 'min_price', 'posted_today']
    test_values =  [
        ["iphone 12 pro", 1000, 10, "y"],
        ["iphone 8 ", 1000, 10, "y"],
        ["iphone 6", 1000, 10, "y"],
    ]
    cases = []
    for item in test_values:
        cases.append(dict(zip(keys,item)))
    basecase = cl.cl_search(cases[0])

    def testSearchWorks(self):
        assert(TestSuite.basecase != None)
    def testStructure(self):
        print(len(TestSuite.basecase.keys()))

    def testBatchShowDict(self):
        dummy = {"query": "iphone 12 pro",
            "item": {
                "name": "iphone 12 dummy item",
                "url": "http://www.disney.com",
                "price": "2000",
                "where": "daMoon"
            }
        }
    def testBatchShowTupleItems(self):
        dummy = {"iphone 12 stupid cl name": ["https://www.barcelonafc.com", "12320", "liverpool"],
            "otherName Something" : ["https://www.google.com", "20", "sfNoeValley"],
        }
        cl.batchShow(dummy, 1, 10)



unittest.main()