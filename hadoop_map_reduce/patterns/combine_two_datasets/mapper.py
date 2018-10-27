#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        # user data
        if len(line)==5:
            if line[0] != 'user_ptr_id':
                writer.writerow(line[0:1]+['A']+line[1:])
            
        # post data
        else:
            if line[0] != 'id':
                writer.writerow(line[0:1]+['B']+line[1:4]+line[5:10])
        
if __name__=='__main__':
    mapper()