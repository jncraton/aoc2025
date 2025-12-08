from itertools import combinations

boxes = [tuple([int(x) for x in line.strip().split(',')]) for line in open('8-1.txt').readlines()]

# Pre-compute all distances, then sort

pairs = []

for a, b in combinations(boxes, 2):
    distance = sum((ai-bi)**2 for ai,bi in zip(a,b))
    pairs.append((distance, a, b))

pairs.sort()

print(pairs)