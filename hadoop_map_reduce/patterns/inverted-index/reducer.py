#!/usr/bin/python
import sys
import re

old_word = None
count = 0
ids = []

for line in sys.stdin:
    data = line.split('\t')
    if len(data) < 2:
        continue

    word= data[0]
    index = int(re.sub('\D','', data[1]))

    if old_word and old_word != word:
        ids_ordered = sorted(list(set(ids)))
        print old_word, '\t', count, '\t', ids_ordered
        ids = []
        count = 0

    old_word = word
    ids.append(index)
    count += 1

if old_word:
    ids_ordered = sorted(list(set(ids)))
    print old_word, '\t', count, '\t', ids_ordered
