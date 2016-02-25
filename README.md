# Python toolkit for Indonesian Tagged Corpus

Example usage:

Work with an interactive shell in Python 3
-----

```
bash itc.sh
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

