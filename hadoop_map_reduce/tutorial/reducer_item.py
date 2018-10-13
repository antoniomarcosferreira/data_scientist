#!/usr/bin/python
import sys

total = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    key, sale = data
    if oldKey and oldKey != key:
        print oldKey, "\t", total
        oldKey = key
        total = 0

    oldKey = key
    total += float(sale)

if oldKey != None:
   print oldKey, "\t", total
