# Python toolkit for Indonesian Tagged Corpus

Example usage:

Work with an interactive shell in Python 3
-----

```
bash itc.sh
```
or 
```
./itc.sh
```
or 
```
export PYTHONSTARTUP=itc.py
python3
```
or 
  ```
bash-3.2$ python3
Python 3.5.1 (default, Jan 22 2016, 08:54:32) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from itctk import *
>>> doc = itc()
```

Find all sentences with the word `tidak` inside
-----

```
tidak_words = doc.find('tidak')
```

Loop through all words in all sentences and do something with those
---
```
for sent in doc:        # for each sentence in doc
  for word in sent:     # for each word in that sentence
    print(word)
```

Look for interesting constructions with `lookup()`.
---
look for words with parts-of-speech.
Do not use upper case in `lookup()` because sentences are in lower case.
When you call `lookup_c()` the result is auto dumped. Use a variable instead, such as `ss`.
e.g.  to search for "aku makan", "aku minum" etc.
and show the results line by line
```
ss = lookup("aku/prp \w+/vb")
```

Look for interesting constructions with `lookup_c()`.
---
When you call `lookup_c()` the result is auto dumped. Use a variable instead, such as `ss`.
```
ss = lookup_c("NEG PRP VB")
```
regular expressions can be used,
e.g. look for constructions with 12 NNP
and show the results line by line
```
ss = lookup_c("(NNP ){12}"))
```
e.g. look for constructions which has any POS
preceded by NEG and followed by VB such as
NEG PRP VB, NEG JJ VB etc.
```
ss = lookup_c("NEG \w+ VB")
```

Look for parts-of-speech constructions in a sentence:
---
```
a_sentence.pos()
```

Print a sentence as a text without part-of-speech information:
---
```
a_sentence.text()
```

Look for a dictionary of unique words and part(s)-of-speech:
---
```
doc.lexicon
```

Look for a dictionary of parts-of-speech and unique word(s):
---
```
doc.pos
```

Look for a dictionary of part-of-speech tagsets, descriptions and examples:
---
```
POS_TAGSET
```
e.g. look for the description and examples of part-of-speech "CC":
```
POS_TAGSET["CC"].desc
POS_TAGSET["CC"].ex
```

Look for a list of parts-of-speech:
---
```
doc.pos_list()
```

Look for a list of words:
---
```
doc.word_list()
```

Look for words in sentences with regular expression:
---
e.g. look for words "penge...kan" such as "pengecekan"
```
doc.find("^penge.+kan$")
```
to show sentence by sentence
```
dump(doc.find("^penge.+kan$"))
```

Look for words without sentences with regular expression:
---
e.g. look for words "penge...kan" such as "pengecekan"
```
doc.find_word("^penge.+kan$")
```
to show line by line
```
dump(doc.find_word("^penge.+kan$"))
```

Print the whole text:
---
```
print(doc.text())
```

Project structure:
---

```
.
|- LICENSE
|- README.md
|- TODO.md
|- docs
|   |-- ...
|- requirements.txt
|- itctk               
|   |-- __init__.py
|   |-- ...
|- test
|   |-- __init__.py
|   |-- ....
|- setup.py
```
