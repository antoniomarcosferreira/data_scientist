#!/usr/bin/python
import sys

paths = dict()

for item in sys.stdin:
    item = item.strip()
    if item in paths:
        paths[item] += 1
    else:
        paths[item] = 1

for key, value in sorted(paths.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
