from itertools import combinations

tiles = [[int(v) for v in l.strip().split(',')] for l in open('9.txt').readlines()]

rects = []

for a, b in combinations(tiles, 2):
    area = (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
    rects.append(tuple([area, a, b]))

rects.sort()

print(rects[-1][0])