#!/usr/bin/env python

import nltk
from nltk.tokenize import sent_tokenize

f = open('_test.txt')
raw = f.read()
sent = sent_tokenize(raw)
print(len(sent))

