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

def show_help():
    usage = [("Command", "Description")
             ,("doc", "`doc` is a special variable to access itc corpus")
             ,('sents = lookup(\'kita/prp \w+/vb\')', 'Look for sentences with kita as PRP that follows by any verb')
             ,("doc.pos_list()", "Get all POS that are used in this corpus")
             ,("doc.find('kita')", "Find all sentences with the word `kita`")
             ,("help(doc)", "Show everything about Document class")
             ,("help(lookup)", "How to use the lookup function")
             ,("POS_TAGSET['CC']", "Show information about the tag `CC`")
    ]
    max_lengths = [0,0]
    for row in usage:
        for idx,cell in enumerate(row):
            if max_lengths[idx] < len(cell):
                max_lengths[idx] = len(cell)

    for row in usage:
        print(' '.join([ text.ljust(size) for size,text in zip(max_lengths, row)]))
    print("Try help(doc), help(Sentence), help(Word), help(lookup), etc. for more information")

def main():
    print("Reading Indonesian Tagged Corpus ...")
    global doc
    doc = itc()
    print("ITC document is now ready to be used in var `doc`")
    stats(doc)
    print('--')
    show_help()
    print('')

if __name__ == '__main__':
    main()
