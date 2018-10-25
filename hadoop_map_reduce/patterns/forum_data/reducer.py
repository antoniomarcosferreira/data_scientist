#!/usr/bin/python
import sys

total = 0
oldWord = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    word, index = data
    if oldWord and oldWord != word:
        print(oldWord, "\t", total)
        oldWord = word
        total = 0

    oldWord = word
    total += 1

if oldWord != None:
   print(oldWord, "\t", total)
