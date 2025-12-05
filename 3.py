banks = [b.strip() for b in open('3.txt').readlines()]

total = 0

for bank in banks:
    best = 0

    for i, a in enumerate(bank):
        for b in bank[i+1:]:
            best = max(best, int(a + b))

    total += best

print(total)