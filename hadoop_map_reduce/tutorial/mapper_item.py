#!/usr/bin/python
import sys

#Instead of breaking sales by store, instead, break sales by product category in all of our stores.
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        # Data cols: date, time, store, item, cost, payment
        print("{0}\t{1}".format(data[3], data[4]))

