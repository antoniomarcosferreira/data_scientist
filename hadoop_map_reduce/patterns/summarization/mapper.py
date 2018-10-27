#!/usr/bin/python

"""
We take the data from the purchases.txt file 
and map the day of the week and the value of the sale
"""

import sys
import csv
from datetime import datetime

lines = csv.reader(sys.stdin, delimiter='\t')

for data in lines:
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print "{0}\t{1}".format(weekday,cost)
