#!/usr/bin/env python3

import sys

#checks only if output has correct flights (ie. are in input)

if len(sys.argv) != 3:
    print("Expecting 2 arguments - 1) Input file, 2) Contestant\'s output file")
    sys.exit(1)

try:
    input = open(sys.argv[1], 'r')
    output = open(sys.argv[2], 'r')
except:
    print("Could not open files")
    sys.exit(1)

output_flights = set()
output_price = 0

output_price = int(output.readline().rstrip())
for l in output.readlines():
    [f, t, d, p] = l.rstrip().split(' ') #From_city, To_city, Day, Price
    d = int(d)
    p = int(p)
    output_flights.add((f, t, d, p))

input_start_city = input.readline().rstrip()
for l in input.readlines():
    [f, t, d, p] = l.rstrip().split(' ') #From_city, To_city, Day, Price
    d = int(d)
    p = int(p)
    if (f, t, d, p) not in output_flights:
        print("Error: Flight on output is not in input")
        sys.exit(1)

