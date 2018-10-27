#!/usr/bin/python

import sys

count = 0
total = 0
oldWeekday = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    weekday, sale = data

    if oldWeekday and oldWeekday != weekday:
        print oldWeekday, "\t", total
        weekday = weekday
        count = 0
        total = 0

    oldWeekday = weekday
    count += 1
    total += float(sale)

if weekday != None:
    print weekday, "\t", total
