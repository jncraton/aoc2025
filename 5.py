fresh, available = open('5.txt').read().split('\n\n')

fresh = [tuple(map(int, f.split('-'))) for f in fresh.split()]
available = [int(a) for a in available.split()]

fresh_count = 0
for a in available:
    for f in fresh:
        if f[0] <= a <= f[1]:
            fresh_count += 1
            break

# Part 2

fresh = sorted(fresh)

fresh_ids_count = 0
next_base = 0
for f in fresh:
    base = max(f[0], next_base)
    fresh_ids_count += max(0, f[1] - base + 1)
    next_base = max(base, f[1] + 1)

print(fresh_ids_count)