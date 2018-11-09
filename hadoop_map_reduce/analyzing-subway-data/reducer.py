#!/usr/bin/python
import sys

def reducer():
    
    old_unit = None
    total_entries = 0
    
    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 2:
            continue
        
        unit, entries = data

        if old_unit and old_unit != unit:
            print old_unit, "\t", int(total_entries)
            total_entries = 0

        old_unit = unit
        total_entries += float(entries)

    if old_unit != None:
        print old_unit, "\t", int(total_entries)
        
sys.stdout = open('reducer_result.txt', 'w')
reducer()
