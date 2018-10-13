#!/usr/bin/python
import sys

total = 0
oldItem = None

for item in sys.stdin:
    item = item.strip()
    if oldItem and oldItem != item:
        print oldItem, "\t", total
        oldItem = item
        total = 0

    oldItem = item
    total += 1

if oldItem != None:
    print oldItem, "\t", total
