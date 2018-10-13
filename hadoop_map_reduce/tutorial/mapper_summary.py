#!/usr/bin/python
import sys

#Find the monetary value for the highest individual sale for each store separately.
#Find the total value of sales in all stores and the total number of sales.
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        # Data cols: date, time, store, item, cost, payment
        print("{0}\t{1}".format(data[2], data[4]))
