#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.split('"')
    if len(data) == 3:
        request_data = data[1].strip().split(" ")
        request_data = request_data[1].strip().replace("http://www.the-associates.co.uk","")
        print request_data


