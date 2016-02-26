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

Look for interesting constructions:
---
```
lookup("NEG PRP VB")
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
