#!/usr/bin/python
import sys
import re
import csv

lines = csv.reader(sys.stdin, delimiter='\t')

for data in lines:

    if len(data) > 3:
        if "<p>" in data[4]:
            text = re.findall(r"[\w']+", data[4])
            words = map(lambda x: x.lower(), text)

            for word in words:
                print word, '\t', data[0]

