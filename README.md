# Rules:
- Find the Hamiltonian cycle in time dependant flight graph 
- You are given:
    - `m` flights flying between `n` cities
    - `n+1` days to visit `n` cities
    - Start/end airport (round trip)
- Being at day `i` in city `x` means you can catch all the flights on day `i+1` from city `x`
- All flights are immediate, they take no time.
- On each day you have to board exactly 1 flight.
- On some days, there might not be a flight between some cities.
- We guarantee, that at least one Hamiltonian cycle in any given graph, exists.

# Program:
- Executable in `/app/run`
- Input will be `STDIN`, output will be `STDOUT`.

## Input, `STDIN`
```
<City to start from>  # always a single IATA code
<FROM> <TO> <DateOfDeparture> <PRICE>
<FROM> <TO> <DateOfDeparture> <PRICE>
...
```
#### e.g.:
```
NAP
NAP BRQ 0 10
FCO BRQ 0 641
BRQ FCO 1 40
BRQ NAP 1 510
FCO NAP 2 3

```

## Output, `STDOUT`
### This will be strictly validated for syntax, and against input.
### Format
- We expect n+1 lines.
- First line will be total price.
- Second to last(n+1) line will contain flights in the same format as the input.

#### e.g.:
```
53
NAP BRQ 0 10
BRQ FCO 1 40
FCO NAP 2 3
```
