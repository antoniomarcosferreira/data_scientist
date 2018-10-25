#!/usr/bin/python
import sys
import re

for line in sys.stdin:
    text = re.sub(r'[^\w\s]', ' ', line.strip())
    text = re.sub('[ +|\t]',' ',text)
    for idx, val in enumerate(text.split(' ')):
        if val.strip() != '':
            print("{0}\t{1}".format(val.strip(), idx))
