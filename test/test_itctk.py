#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script for testing ITCtk library
Latest version can be found at https://github.com/neocl/itctk

References:
    Python documentation:
        https://docs.python.org/
    Python unittest
        https://docs.python.org/3/library/unittest.html
    --
    argparse module:
        https://docs.python.org/3/howto/argparse.html
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
'''

# Copyright (c) 2016, Le Tuan Anh <tuananh.ke@gmail.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

__author__ = "Le Tuan Anh <tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2016, itctk"
__credits__ = [ "Le Tuan Anh" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

########################################################################

import sys
import os
import argparse
import unittest
from itctk import itc
from itctk import Document, Sentence, Word
from itctk import ITC_DATA_FILE, parse_data   # Expose low level functions

########################################################################

class TestICTTK(unittest.TestCase):

    def test_read_doc(self):
        print("Testing read all ITC content")
        doc = itc('data/test.tsv')
        self.assertIsNotNone(doc)
        # self.assertEqual(len(doc.sentences), 10030) # real data
        self.assertEqual(len(doc.sentences), 24)      # test data
        
class TestWord(unittest.TestCase):

    def test_word_comparison(self):
        w = Word('test', 'NN')
        w2 = Word('test', 'NN')
        self.assertTrue(w == w2)

    def test_word_sorting(self):
        w1 = Word(None, None)
        w2 = Word(None, None)
        w3 = Word('test', 'NN')
        w4 = Word('test', 'VB')
        
        self.assertTrue(w1 == w2)
        self.assertTrue(w4 > w3)
        self.assertTrue(w3 > w2)

        print("Test list sorting ...")
        l = [w4, w3, w2, w1]
        sorted_l = list(sorted(l))
        expected = [w1, w2, w3, w4]
        self.assertEqual(expected, sorted_l)
                

    def test_word_in_set(self):
        set1 = set()
        set2 = set()
        w1 = Word(None, None)
        w2 = Word(None, None)
        w3 = Word('test', 'NN')
        w4 = Word('test', 'VB')

        set1.add(w1)
        set1.add(w2)
        set1.add(w3)
        
        # w1 and w2 are the same
        self.assertEqual(2, len(set1))

        set2.add(w1)
        set2.add(w2)
        set2.add(w3)
        set2.add(w4)

        self.assertEqual(3,len(set2))

    def test_word_search(self):
        '''Test searching by regular expression'''
        doc = itc('data/test.tsv')
        found = doc.find_word('mem.+')
        self.assertTrue(len(found) > 0)
        self.assertEqual(7, len(found))

########################################################################

def main():
    unittest.main()

if __name__ == "__main__":
    main()
