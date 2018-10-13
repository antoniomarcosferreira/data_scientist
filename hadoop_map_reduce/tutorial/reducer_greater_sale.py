#!/usr/bin/python
import sys

greaterSale = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    key, sale = data
    if oldKey and oldKey != key:
        print oldKey, "\t", greaterSale
        oldKey = key
        greaterSale = 0

    oldKey = key
    if greaterSale < float(sale):
        greaterSale = float(sale)

if oldKey != None:
   print oldKey, "\t", greaterSale
