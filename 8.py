from itertools import combinations
from collections import Counter
from math import prod

boxes = [tuple([int(x) for x in line.strip().split(',')]) for line in open('8.txt').readlines()]

# Pre-compute all distances, then sort

pairs = []

for a, b in combinations(boxes, 2):
    distance = sum((ai-bi)**2 for ai,bi in zip(a,b))
    pairs.append((distance, a, b))

pairs.sort()

circuits = {}
next_circuit = 0
trace = tuple()

for distance, a, b in pairs[:1000]:
    if circuits.get(a) in trace or circuits.get(b) in trace:
        print('start', distance, a, b, circuits.get(a), circuits.get(b)) 

    if a in circuits and b in circuits:
        # Replace circuit b id to circuit a id
        old_id = circuits[b]
        for box in list(circuits.keys()):
            if circuits[box] == old_id:
                circuits[box] = circuits[a]
        if circuits.get(a) in trace or circuits.get(b) in trace:
            print('merged', distance, a, b, circuits[a], circuits[b]) 
    elif a in circuits:
        circuits[b] = circuits[a]
        if circuits.get(a) in trace or circuits.get(b) in trace:
            print('set b', distance, a, b, circuits[a], circuits[b]) 
    elif b in circuits:
        circuits[a] = circuits[b]
        if circuits.get(a) in trace or circuits.get(b) in trace:
            print('set a', distance, a, b, circuits[a], circuits[b]) 
    else:
        circuits[a] = next_circuit
        circuits[b] = next_circuit
        next_circuit += 1
        if circuits.get(a) in trace or circuits.get(b) in trace:
            print('new', distance, a, b, circuits[a], circuits[b]) 

    if circuits[a] in trace or circuits[b] in trace:
        print('end', distance, a, b, circuits[a], circuits[b]) 

counts = Counter(circuits.values())

total = prod(count for _, count in counts.most_common(3))

print(total)