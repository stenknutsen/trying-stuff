

import nltk, re, pprint

from nltk.tokenize import sent_tokenize
from nltk import *
from nltk.corpus import reuters

f = open('test.txt')



raw = f.read()

tokenSent = sent_tokenize(raw)

#print(tokenSent)
##print(posTagged)


wordTokens = word_tokenize(tokenSent[2])
print(wordTokens)

posTagged = pos_tag(wordTokens)
print(posTagged)


