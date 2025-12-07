rows = [r.strip() for r in open('7.txt').readlines()]

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

print(splits)