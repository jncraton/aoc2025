from itertools import combinations
from collections import Counter
from math import prod

boxes = [
    tuple([int(x) for x in line.strip().split(",")])
    for line in open("8.txt").readlines()
]

# Pre-compute all distances, then sort

pairs = []

for a, b in combinations(boxes, 2):
    distance = sum((ai - bi) ** 2 for ai, bi in zip(a, b))
    pairs.append((distance, a, b))

pairs.sort()

circuits = {}
next_circuit = 0

for distance, a, b in pairs[:1000000]:
    if a in circuits and b in circuits:
        # Replace circuit b id to circuit a id
        old_id = circuits[b]
        for box in list(circuits.keys()):
            if circuits[box] == old_id:
                circuits[box] = circuits[a]
    elif a in circuits:
        circuits[b] = circuits[a]
    elif b in circuits:
        circuits[a] = circuits[b]
    else:
        circuits[a] = next_circuit
        circuits[b] = next_circuit
        next_circuit += 1

    if Counter(circuits.values()).most_common(1)[0][1] == len(boxes):
        print(a[0] * b[0])
        break

# total = prod(count for _, count in counts.most_common(3))
# print(total)
