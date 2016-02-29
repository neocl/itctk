#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Python toolkit for manipulating Indonesian Tagged Corpus
Latest version can be found at https://github.com/neocl/itctk

References:
    Python documentation:
        https://docs.python.org/
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
__contributors__ = ["David Moeljadi <davidmoeljadi@gmail.com>"]
__copyright__ = "Copyright 2016, itctk"
__credits__ = [ "Le Tuan Anh" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Le Tuan Anh"
__email__ = "<tuananh.ke@gmail.com>"
__status__ = "Prototype"

########################################################################

from itctk import *
import re
from collections import defaultdict as dd

########################################################################
# Some useful methods
########################################################################

def dump(a_list):
    for idx,item in enumerate(a_list):
        print("%s. %s" % (idx + 1, item))

def pro_lookup(cond):
    sents = [ x for x in doc if cond(x) ]
    dump(sents)
    return Document(sents)

# [ 2016-02-29 DM ] added a better lookup method
def lookup_c(pattern_text):
    pattern = re.compile(pattern_text)
    return pro_lookup(lambda x: pattern.search(x.pos()))

def lookup(pattern_text):
    '''to search words with parts-of-speech
    e.g. lookup("aku/prp \w+/vb") to search for "aku makan", "aku minum" etc.
    Do not use upper case in lookup() because sentences are in lower case.'''
    pattern = re.compile(pattern_text)
    return pro_lookup(lambda x: pattern.search(str(x).lower()))

def stats(doc):
    print("Sentence count: {:>12,}".format(len(doc)))
    print("Token count   : {:>12,}".format(len(doc.words)))
    print("Lexicon size  : {:>12,}".format(len(doc.word_list())))
    print("POS tagset    : {}".format(doc.pos_list()))
    print()

########################################################################
# Load ITC into doc by default
########################################################################

doc = None # ITC will be loaded into this variable

def main():
    print("Reading Indonesian Tagged Corpus ...")
    global doc
    doc = itc()
    print("ITC document is now ready to be used in var `doc`")
    stats(doc)

if __name__ == '__main__':
    main()
