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

        target = [
            ('WORD', 'to'),
            ('WORD', 'sentence'),
            ('WORD', 'here'),
            ('INTEGER', 12),
            ('TAG_MARKER', ':'),
            ('INTEGER', 30),
            ('INTEGER', 3),
            ('TIME_UNIT', 'h'),
            ('INTEGER', 15),
            ('TIME_UNIT', 'min'),
            ('WORD', 'tags'),
            ('TAG_MARKER', ':'),
            ('WORD', 'tag1'),
            ('WORD', 'tag3'),
            ('WORD', 'tag4'),
            ]

        tok = tokenizer(e1)

        self.assertEqual(tok.get_token_list(), target)
        self.assertEqual(tok.tag_marker_count, 2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTokenizer)
    unittest.TextTestRunner(verbosity=3).run(suite)
