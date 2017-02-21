import sys

if len(sys.argv) != 3:
    print("Expecting 2 arguments - 1) Input file, 2) Contestant\'s output file")
    sys.exit(1)

try:
    input = open(sys.argv[1], 'r')
    output = open(sys.argv[2], 'r')
except:
    print("Could not open files")
    sys.exit(1)

input_cities = set()
input_flights = dict()
input_start_city = ''

input_start_city = input.readline().rstrip()
for l in input.readlines():
    [f, t, d, p] = l.rstrip().split(' ') #From_city, To_city, Day, Price
    d = int(d)
    p = int(p)

    if (f, t, d) in input_flights:
        print("Input contains two same flights at same day")
        sys.exit(1)
    else:
        input_flights[(f, t, d)] = p
    input_cities.add(f)
    input_cities.add(t)

output_flights = list()
output_price = 0
calculated_price = 0

output_price = int(output.readline().rstrip())
for l in output.readlines():
    [f, t, d, p] = l.rstrip().split(' ') #From_city, To_city, Day, Price
    d = int(d)
    p = int(p)

    if (f, t, d) not in input_flights:
        print("Error: Flight on output is not in input")
        sys.exit(1)
    calculated_price += input_flights[(f, t, d)]
    output_flights.append((f, t, d))

if calculated_price != output_price:
    print("Error: Price is not good")
    sys.exit(1)

# check if flight sequence is good
for i in range(len(output_flights)):
    if output_flights[i][1] != output_flights[(i+1)%len(output_flights)][0]:
        print("Error: Sequence of flights is not good")
        sys.exit(1)

#check if starting city is good
if input_start_city != output_flights[0][0]:
    print("Error: Starting city is wrong")
    sys.exit(1)

#check ending city
if input_start_city != output_flights[-1][1]:
    print("Error: Ending city is not equal starting city")
    sys.exit(1)

#check that each flight departures on good day
for i in range(len(output_flights)):
    if output_flights[i][2] != i:
        print("Flights departures on wrong day")
        sys.exit(1)

#check that each city is visited
if len(input_cities) != len(output_flights):
    print("Not each city is visited")
    sys.exit(1)
