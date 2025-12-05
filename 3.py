from functools import cache

banks = [b.strip() for b in open('3.txt').readlines()]

total = 0

@cache
def best_joltage(bank, n):
    if n == 0:
        return ''

    best = 0

    for i, val in enumerate(bank):
        best = max(best, int(val + best_joltage(bank[i+1:], n-1)))

    return str(best or '')

for bank in banks:
    best = best_joltage(bank, 12)

    print(best)
    total += int(best)

print(total)