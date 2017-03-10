# Rules:
- Find the Hamiltonian cycle in time dependent flight graph
- You are given:
    - `m` flights flying between `n` cities
    - `n` days to visit `n` cities
    - Start/end airport (round trip)
- Being at day `i` in city `x` means you can catch all the flights on day `i+1` from city `x`
- All flights are immediate, they take no time.
- On each day you have to board exactly 1 flight.
- On some days, there might not be a flight between some cities.
- We guarantee, that at least one Hamiltonian cycle in any given graph, exists.

# Evaluation
- You have 30 seconds for each dataset to produce valid output. After this period we kill your program if it hadn't already finished and process what your program outputted up to this point. Invalid output will result in 0 points but killing your program as such doesn't affect awarded points as long as you manage to produce valid result. Detailed description of our scoring system can be found in [scoring README](scoring_system/README.md).
- Evaluation data will be sampled the same way as the training [real data](real_data) - we will use real world prices of flights.

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
Some remarks about input:
 - `<FROM>`, `<TO>` - IATA codes - 3 English alphabet uppercase letters A-Z.
 - `<PRICE>` will be positive integer that fits into `uint16_t` - 16 bit unsigned integer (0 < `<PRICE>` <= 65535). (No prefixes, no hexa, nothing. Just number. :-])
 - Input data will be ordered lexicographically `(FROM, TO, DateOfDeparture)`,
 with `FROM/TO` ordering to be also lexicographical. If this seems to be
 confusing, just look at the output of `data_generator.py`.

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

