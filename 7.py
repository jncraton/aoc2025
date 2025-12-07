rows = [r.strip() for r in open('7-1.txt').readlines()]

beams = {rows[0].find('S')}
rows = rows[1:]

splits = 0

for row in rows:
    for beam in beams.copy():
        if row[beam] == '^':
            beams.remove(beam)
            beams.add(beam-1)
            beams.add(beam+1)
            splits += 1

#print(splits)

# Part 2

from collections import Counter

rows = [r.strip() for r in open('7.txt').readlines()]
beams = Counter([rows[0].find('S')])
rows = rows[1:]

for row in rows:
    for beam, count in beams.copy().items():
        if row[beam] == '^' and count > 0:
            beams[beam] -= count
            beams[beam-1] += count
            beams[beam+1] += count

print(sum(count for _, count in beams.items()))

