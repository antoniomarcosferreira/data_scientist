#!/usr/bin/python
import sys

def mapper():

    first_line = True
    for line in sys.stdin:

        if first_line == True:
            first_line = False
            continue

        data = line.strip().split(',')
        if len(data) < 7:
            continue

        print "{0}\t{1}".format(data[1],data[6])


#sys.stdout = open('mapper_result.txt', 'w')
mapper()
