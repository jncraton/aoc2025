rotations = open('1.txt').readlines()

rotations = [int(r.strip().replace('L', '-').replace('R', '')) for r in rotations]

dial = 50
zeroes = 0

for rotation in rotations:
    dial = (dial + rotation) % 100

    if dial == 0:
        zeroes += 1

print(zeroes)
