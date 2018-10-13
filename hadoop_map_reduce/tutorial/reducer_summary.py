#!/usr/bin/python
import sys

totalVal = 0
totalSales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    key, sale = data
    totalVal += float(sale)
    totalSales += 1

print totalSales, "\t", totalVal
