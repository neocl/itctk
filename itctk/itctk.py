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
from collections import namedtuple

#-----------------------------------------------------------------------
# CONFIGURATION
#-----------------------------------------------------------------------
ITC_DATA_FILE = 'data/itcdata/Indonesian_Manually_Tagged_Corpus.tsv'

#-----------------------------------------------------------------------
# POS TAGSET
#-----------------------------------------------------------------------

TagInfo = namedtuple('TagInfo', ['pos', 'desc', 'ex'])

POS_TAGSET = {}
POS_TAGSET["CC"] = TagInfo("CC", """Coordinating conjunction, also called coordinator.
Coordinating conjunction links two or more syntactically equivalent parts of a sentence. Coordinating conjunction can link independent clauses, phrases, or words.""", "dan, tetapi, atau")

POS_TAGSET["CD"] = TagInfo("CD", """Cardinal number.
Cardinal numbers, i.e. numerals which are the answers to the question “How much?” or “How many?”, include:
a. cardinal units, e.g. dua ‘two’,
b. group numbers, e.g. juta ‘million’,
c. full numbers, e.g. enam ‘six’ and 7916,
d. fractions, e.g. sepertiga ‘one-third’,
e. decimal numbers, e.g. 0,025 and 0,525,
f. indefinite numbers, e.g. banyak ‘many’,
g. collective numbers, e.g. kedua ‘both’,
berpuluh-puluh ‘tens’, and ribuan ‘thousands’,
h. dates, and
i. years.""", "dua, juta, enam, 7916, sepertiga, 0,025, 0,525, banyak, kedua, ribuan, 2007, 25")

POS_TAGSET["OD"] = TagInfo("OD", """Ordinal number.
Ordinal number indicates an ordered position in a series, e.g. ketiga ‘third’.""", "ketiga, ke-4, pertama")

POS_TAGSET["DT"] = TagInfo("DT", """Determiner / article.
Article is a determiner, i.e. grammatical unit which limits the potential referent of a noun phrase, whose basic role is to mark noun phrases as either definite or indefinite.""", "para, sang, si")

POS_TAGSET["FW"] = TagInfo("FW", """Foreign word.
Foreign word is a word which comes from foreign language and basically is not yet included in Indonesian dictionary.
If a foreign word is part of a proper noun or name, that word will be labeled NNP.""", "climate change, terms and conditions")

POS_TAGSET["IN"] = TagInfo("IN", """Preposition.
A preposition links word or phrase and constituent in front of that preposition and results prepositional phrase.""", "dalam, dengan, di, ke, oleh, pada, untuk")

POS_TAGSET["JJ"] = TagInfo("JJ", """Adjective.
Adjectives, i.e. words which describe, modify, or specify some properties of the head noun of the phrase, include:
a. conditions, e.g. bersih ‘clean’,
b. sizes, e.g. panjang ‘long’ and kecil ‘small’,
c. colors, e.g. hitam ‘black’,
d. durations, e.g. lama ‘long (duration)’,
e. distances, e.g. jauh ‘far’,
f. emotions or feelings, e.g. marah ‘angry’,
g. senses, e.g. manis ‘sweet’,
h. membership of a group, e.g. nasional
‘national’, and
i. shapes, e.g. bulat ‘round’.""", "bersih, panjang, hitam, lama, jauh, marah, suram, nasional, bulat")

POS_TAGSET["MD"] = TagInfo("MD", """Modal and auxiliary verb.""", "boleh, harus, sudah, mesti, perlu")

POS_TAGSET["NEG"] = TagInfo("NEG", """Negation.""", "tidak, belum, jangan")

POS_TAGSET["NN"] = TagInfo("NN", """Noun.
Nouns, i.e. words which refer to human, animal, thing, concept, or understanding, include:
a. flora and fauna, e.g. monyet ‘monkey’,
b. locative nouns and nouns which indicate a
place or direction, e.g. bawah ‘beneath’,
c. nouns which indicate time, e.g. sekarang
‘now’, and
d. currencies which are not written in the form of
symbols, e.g. rupiah.""", "monyet, bawah, sekarang, rupiah")

POS_TAGSET["NNP"] = TagInfo("NNP", """Proper noun.
Proper noun is a specific name of a person, thing, or place. Proper nouns include:
a. personal name, e.g. Boediono,
b. the name of a geographical place, e.g. Laut
Jawa,
c. the name of a country, state, or region, e.g.
Indonesia,
d. the name of organization, institution, or
company, e.g. Bank Mandiri,
e. stock symbols, e.g. BBKP,
f. the names of months, e.g. Januari,
g. the days of the week, e.g. Senin,
h. the name of the feast, e.g. Idul Fitri,
i. the name of competition, championship,
award, or historical event, e.g. Piala Dunia, and
j. the title of a work, television show, or movie, e.g. Lord of the Rings: The Return of the King.
Proper noun which is written in foreign language is labeled NNP.
Abbreviated proper noun is labeled NNP.
If a proper noun consists of more than one words or parts, each word or part of that proper noun will be labeled NNP.""", "Boediono, Laut Jawa, Indonesia, India, Malaysia, Bank Mandiri, BBKP, Januari, Senin, Idul Fitri, Piala Dunia, Liga Primer, Lord of the Rings: The Return of the King")

POS_TAGSET["NND"] = TagInfo("NND", """Classifier, partitive, and measurement noun. Classifiers classify nouns into particular noun
class, e.g. orang ‘man’.
Partitives indicate particular amount of something based on the way it is measured, assembled, or processed, e.g. tetes ‘drop’.
Measurement nouns refer to size, distance, volume, speed, weight, or temperature, e.g. ton ‘ton’.""", "orang, ton, helai, lembar")

POS_TAGSET["PR"] = TagInfo("PR", """Demonstrative pronoun .
Demonstrative pronouns imply “pointing to” or “demonstrating” the object they refer to, e.g. ini ‘this’.""", "ini, itu, sini, situ")

POS_TAGSET["PRP"] = TagInfo("PRP", """Personal pronoun.
Personal pronouns, i.e. pronouns which refer to people, include:
a. the first person singular pronoun, e.g. saya ‘I’,
b. the first person exclusive plural pronoun, e.g.
kami ‘we (exclusive)’,
c. the first person inclusive plural pronoun, e.g.
kita ‘we (inclusive)’,
d. the second person singular pronoun, e.g. kamu
‘you’,
e. the second person plural pronoun, e.g. kalian
‘you plural’,
f. the third person singular pronoun, e.g. dia ‘he,
she’, and
g. the third person plural pronoun, e.g. mereka
‘they’.""", "saya, kami, kita, kamu, kalian, dia, mereka")

POS_TAGSET["RB"] = TagInfo("RB", """Adverb.""", "sangat, hanya, justru, niscaya, segera")

POS_TAGSET["RP"] = TagInfo("RP", """Particle.
In this research, POS tag RP marks emphatic particle, i.e. particle which confirms interrogative, imperative, or declarative sentences.""", "pun, -lah, -kah")

POS_TAGSET["SC"] = TagInfo("SC", """Subordinating conjunction, also called subordinator.
Subordinating conjunction links two or more clauses and one of the clauses is a subordinate clause.""", "sejak, jika, seandainya, supaya, meski, seolah- olah, sebab, maka, tanpa, dengan, bahwa, yang, lebih ... daripada ..., semoga")

POS_TAGSET["SYM"] = TagInfo("SYM", """Symbol.
Symbols, which are labeled SYM, include mathematical symbols, e.g. +, and currency symbols, e.g. IDR.""", "IDR, +, %, @")

POS_TAGSET["UH"] = TagInfo("UH", """Interjection.
Interjection expresses feeling or state of mind and has no relation with other words syntactically.""", "brengsek, oh, ooh, aduh, ayo, mari, hai")

POS_TAGSET["VB"] = TagInfo("VB", """Verbs.
Verbs, which are labeled VB, include transitive verbs, intransitive verbs, active verbs, passive verbs, and copulas.
If a verb consists of foreign word verb and Indonesian affixes, the resulted verb is labeled VB, e.g. di-arrange ‘arranged’.""", "merancang, mengatur, pergi, bekerja, tertidur")

POS_TAGSET["WH"] = TagInfo("WH", """Question.
Question word distinguishes sentence as interrogative.
A question, called indirect question, can be placed within a declarative sentence as subordinate clause. Thus, question word, which links indirect question and the main clause in a declarative sentence, becomes subordinating conjunction and is labeled SC.""", "siapa, apa, mana, kenapa, kapan, di mana, bagaimana, berapa")

POS_TAGSET["X"] = TagInfo("X", """Unknown.
A word or part of a sentence which its category is unknown or uncertain is labeled X.
Typo is also labeled X.""", "statemen")

POS_TAGSET["Z"] = TagInfo("Z", """Punctuation.""", ""...", ?, .")

#----------------------------------------------------------------------------
# DATA STRUCTURES
#----------------------------------------------------------------------------

class Document:
    ''' A document contains many sentences
    '''
    def __init__(self, sentences = None):
        self.words     = []
        self.lexicon   = defaultdict(set)
        self.pos       = defaultdict(set)

        if sentences is None:
            self.sentences = []
        else:
            self.sentences = sentences
            # auto add all words in provided sentences into this doc
            for sent in sentences:
                for word in sent:
                    self.add_word(word)


    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, index):
        return self.sentences[index]

    def __iter__(self):
        for sent in self.sentences:
            yield sent

    def __repr__(self):
        return str(self.sentences)

    def new_sentence(self):
        ''' Create a new sentence
        '''
        sent = Sentence(self)
        self.sentences.append(sent)
        return sent

    def add_word(self, word):
        ''' Add a word into sentence. Normally you should NOT call this method.
        '''
        self.words.append(word)
        self.lexicon[word.text.lower()].add(word.pos)
        self.pos[word.pos].add(word.text.lower())

    def word_list(self):
        ''' Return a list of distinct word (as string, not word object) in ITC
        '''
        return list(sorted(self.lexicon.keys()))

    def pos_list(self):
        ''' Return a list of all POS that are used in the corpus
        Currently: ['CC', 'CD', 'DT', 'FW', 'IN', 'JJ', 'MD', 'NEG', 'NN', 'NND', 'NNP', 'OD', 'PR', 'PRP', 'RB', 'RP', 'SC', 'SYM', 'UH', 'VB', 'WH', 'X', 'Z']
        '''
        return list(sorted(self.pos.keys()))

    def text(self):
        ''' Return a text-only version of this doc
        '''
        return '\n'.join([ x.text() for x in self ])

    def find(self, text, case_sensitive=True):
        words = self.find_word(text, case_sensitive)
        sents = set([ x.sentence for x in words ])
        subdoc = Document(list(sents))
        return subdoc

    def filter(self, pattern_text):
        pattern = re.compile(pattern_text)
        

    def find_word(self, text, case_sensitive=True):
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
        ''' Add a new word and register this sentence as its container
        '''
        w = Word(text, pos, self)
        self.words.append(w)
        if self.doc:
            self.doc.add_word(w)
        return w
    
    def text(self):
        ''' Return text-only version of this sentence
        E.g.:
            str(a_sentence) will provide 'Kera/NN untuk/SC amankan/VB pesta olahraga/NN'
            but a_sentence.text() will provide 'Kera untuk amankan pesta olahraga'
        '''
        return " ".join([ x.text for x in self.words ])

    def pos(self):
        ''' Return sentence structure (a sequence of POS as a string)
        E.g.
        pos_struct of the sentence Kera/NN untuk/SC amankan/VB pesta olahraga/NN
        is 
        'NN SC VB NN'
        '''
        return ' '.join([ x.pos for x in self.words ])

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

def export_itc():
    print("Reading ITC ...")
    doc = itc()
    output_loc = 'data/itc.txt'

    print("Exporting ITC ...")
    with open(output_loc, 'w') as itc_output:
        for sent in doc:
            itc_output.write('%s\n' % (sent,))
    print("ITC has been exported to %s" % (output_loc,))
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
        parser.add_argument('-x', '--export', help='Export ITC to NTLK format', action='store_true')

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
                if args.export:
                    export_itc()
                else:
                        parser.print_help()
        pass

if __name__ == "__main__":
        main()
