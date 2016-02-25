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
import re
from collections import defaultdict

#-----------------------------------------------------------------------
# CONFIGURATION
#-----------------------------------------------------------------------
ITC_DATA_FILE = 'data/itcdata/Indonesian_Manually_Tagged_Corpus.tsv'

#----------------------------------------------------------------------------
# DATA STRUCTURES
#----------------------------------------------------------------------------

class Document:
    ''' A document contains many sentences
    '''
    def __init__(self):
        self.sentences = []
        self.words     = []
        self.lexicon   = defaultdict(set)
        self.pos       = defaultdict(set)

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, index):
        return self.sentences[index]

    def __iter__(self):
        for sent in self.sentences:
            yield sent

    def new_sentence(self):
        sent = Sentence(self)
        self.sentences.append(sent)
        return sent

    def add_word(self, word):
        self.words.append(word)
        self.lexicon[word.text.lower()].add(word.pos)
        self.pos[word.pos].add(word.text.lower())

    def word_list(self):
        return list(sorted(self.lexicon.keys()))

    def pos_list(self):
        return list(sorted(self.pos.keys()))

    def find(self, text, case_sensitive=True):
        ''' Find a word by regular expression
        '''
        pattern = re.compile(text)
        if case_sensitive:
            return [ w for w in self.words if pattern.match(w.text) ]
        else:
            return [ w for w in self.words if pattern.match(w.text.lower()) ]

class Sentence:
    ''' Sentence structure
    Words can be accessed by using sent.words (as a list)
    '''

    def __init__(self, doc=None):
        self.words = []
        self.doc   = doc

    def __str__(self):
        return " ".join([ str(x) for x in self.words ])

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __iter__(self):
        for w in self.words:
            yield w

    def new_word(self, text, pos):
        w = Word(text, pos, self)
        self.words.append(w)
        if self.doc:
            self.doc.add_word(w)
        return w
    
    def text(self):
        return " ".join([ x.text for x in self.words ])

class Word:
    ''' Information of a Word
    '''

    def __init__(self, text, pos, sentence=None):
        self.text = text
        self.pos  = pos
        self.sentence = sentence

    def __str__(self):
        return "%s/%s" % (self.text, self.pos)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.text, self.pos))

    def __lt__(self, other):
        return (self.text, self.pos) < (other.text, other.pos)

#----------------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------------

def parse_data(datafile_path):
    doc = Document()
    with open(datafile_path, 'r') as datafile:
        # Read file content
        content = datafile.read()

        # Split into sentences
        sentences_raw = content.split('\n\n') # Sentences are separated by an empty line (\n\n)
        for sentence_raw in sentences_raw:
            words_raw = sentence_raw.split('\n')
            sentence  = doc.new_sentence()
            for word_raw in words_raw:
                if '\t' not in word_raw:
                    continue
                text, pos = word_raw.split('\t')  # Word features are seperated by tabs \t
                word = sentence.new_word(text, pos)

    return doc

########################################################################

def itc(file_name=ITC_DATA_FILE):
    return parse_data(file_name)

def dev_mode():
    print("Find negative words")
    doc = all_ict()
    neg_words = [ 'tidak', 'tak', 'non', 'bukan', 'jangan', 'belum' ]
    word_list = set()
    for sent in doc.sentences:
        for word in sent.words:
            if word.text[:5] in neg_words or word.text[:3] in neg_words:
                word_list.add(str(word).lower())
    print(word_list)

########################################################################

def main():
        '''Main entry of ITCtk.
        '''

        # It's easier to create a user-friendly console application by using argparse
        # See reference at the top of this script
        parser = argparse.ArgumentParser(description="Python toolkit for manipulating Indonesian Tagged Corpus")
        
        # Positional argument(s)
        parser.add_argument('-d', '--dev_mode', help='Quick dev method', action='store_true')

        # Optional argument(s)
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbose", action="store_true")
        group.add_argument("-q", "--quiet", action="store_true")

        # Main script
        if len(sys.argv) == 1:
                # User didn't pass any value in, show help
                parser.print_help()
        else:
                # Parse input arguments
                args = parser.parse_args()
                # Now do something ...
                if args.dev_mode:
                        dev_mode()
                else:
                        parser.print_help()
        pass

if __name__ == "__main__":
        main()
