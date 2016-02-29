#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This file contains information of part-of-speech tagsets.
Latest version can be found at https://github.com/neocl/itctk

References:
    Tagset documentation:
        http://bahasa.cs.ui.ac.id/postag/downloads/Tagset.pdf

@author: David Moeljadi <davidmoeljadi@gmail.com>
'''

# Copyright (c) 2016, David Moeljadi <davidmoeljadi@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__author__ = "David Moeljadi <davidmoeljadi@gmail.com>"
__copyright__ = "Copyright 2016, itctk"
__credits__ = ["David Moeljadi"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "David Moeljadi"
__email__ = "<davidmoeljadi@gmail.com>"
__status__ = "Prototype"

########################################################################

from collections import namedtuple

# -----------------------------------------------------------------------
# POS TAGSET
# -----------------------------------------------------------------------

TagInfo = namedtuple('TagInfo', ['pos', 'desc', 'ex'])

POS_TAGSET = {}

# [2016-02-25 DM] information extracted from http://bahasa.cs.ui.ac.id/postag/downloads/Tagset.pdf

POS_TAGSET["CC"] = TagInfo("CC", """Coordinating conjunction, also called coordinator.
Coordinating conjunction links two or more syntactically equivalent parts of a sentence. Coordinating conjunction can link independent clauses, phrases, or words.""",
                           "dan, tetapi, atau")

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
Article is a determiner, i.e. grammatical unit which limits the potential referent of a noun phrase, whose basic role is to mark noun phrases as either definite or indefinite.""",
                           "para, sang, si")

POS_TAGSET["FW"] = TagInfo("FW", """Foreign word.
Foreign word is a word which comes from foreign language and basically is not yet included in Indonesian dictionary.
If a foreign word is part of a proper noun or name, that word will be labeled NNP.""",
                           "climate change, terms and conditions")

POS_TAGSET["IN"] = TagInfo("IN", """Preposition.
A preposition links word or phrase and constituent in front of that preposition and results prepositional phrase.""",
                           "dalam, dengan, di, ke, oleh, pada, untuk")

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
If a proper noun consists of more than one words or parts, each word or part of that proper noun will be labeled NNP.""",
                            "Boediono, Laut Jawa, Indonesia, India, Malaysia, Bank Mandiri, BBKP, Januari, Senin, Idul Fitri, Piala Dunia, Liga Primer, Lord of the Rings: The Return of the King")

POS_TAGSET["NND"] = TagInfo("NND", """Classifier, partitive, and measurement noun. Classifiers classify nouns into particular noun
class, e.g. orang ‘man’.
Partitives indicate particular amount of something based on the way it is measured, assembled, or processed, e.g. tetes ‘drop’.
Measurement nouns refer to size, distance, volume, speed, weight, or temperature, e.g. ton ‘ton’.""",
                            "orang, ton, helai, lembar")

POS_TAGSET["PR"] = TagInfo("PR", """Demonstrative pronoun .
Demonstrative pronouns imply “pointing to” or “demonstrating” the object they refer to, e.g. ini ‘this’.""",
                           "ini, itu, sini, situ")

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
In this research, POS tag RP marks emphatic particle, i.e. particle which confirms interrogative, imperative, or declarative sentences.""",
                           "pun, -lah, -kah")

POS_TAGSET["SC"] = TagInfo("SC", """Subordinating conjunction, also called subordinator.
Subordinating conjunction links two or more clauses and one of the clauses is a subordinate clause.""",
                           "sejak, jika, seandainya, supaya, meski, seolah- olah, sebab, maka, tanpa, dengan, bahwa, yang, lebih ... daripada ..., semoga")

POS_TAGSET["SYM"] = TagInfo("SYM", """Symbol.
Symbols, which are labeled SYM, include mathematical symbols, e.g. +, and currency symbols, e.g. IDR.""",
                            "IDR, +, %, @")

POS_TAGSET["UH"] = TagInfo("UH", """Interjection.
Interjection expresses feeling or state of mind and has no relation with other words syntactically.""",
                           "brengsek, oh, ooh, aduh, ayo, mari, hai")

POS_TAGSET["VB"] = TagInfo("VB", """Verbs.
Verbs, which are labeled VB, include transitive verbs, intransitive verbs, active verbs, passive verbs, and copulas.
If a verb consists of foreign word verb and Indonesian affixes, the resulted verb is labeled VB, e.g. di-arrange ‘arranged’.""",
                           "merancang, mengatur, pergi, bekerja, tertidur")

POS_TAGSET["WH"] = TagInfo("WH", """Question.
Question word distinguishes sentence as interrogative.
A question, called indirect question, can be placed within a declarative sentence as subordinate clause. Thus, question word, which links indirect question and the main clause in a declarative sentence, becomes subordinating conjunction and is labeled SC.""",
                           "siapa, apa, mana, kenapa, kapan, di mana, bagaimana, berapa")

POS_TAGSET["X"] = TagInfo("X", """Unknown.
A word or part of a sentence which its category is unknown or uncertain is labeled X.
Typo is also labeled X.""", "statemen")

POS_TAGSET["Z"] = TagInfo("Z", """Punctuation.""", '"...", ?, .')
