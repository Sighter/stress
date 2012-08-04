#!/usr/bin/python2

# tests.py -- test file
# @Author:      The Sighter (sighter@resource-dnb.de)
# @License:     GPL
# @Created:     2012-07-24.
# @Revision:    0.1

import unittest

from tokenizer import tokenizer

class TestTokenizer(unittest.TestCase):

    def setUp(self):
        pass

    def test_tokenizer(self):
        e1 = "to sentence here 12:30 3h 15min tags:tag1,tag3 , tag4"
        e2 = "plain todo"

        tok = tokenizer(e1)
        for e in tok.get_token_list():
            print e

        
        
        #self.assertEqual(str(c), "Herbert Claus Naumann -- Ukutuko")

        #self.assertEqual(c.get_full_name(), "Herbert Claus Naumann")
 

if __name__ == '__main__':
    unittest.main()
