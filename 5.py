fresh, available = open('5-1.txt').read().split('\n\n')

fresh = [list(map(int, f.split('-'))) for f in fresh.split()]
available = [int(a) for a in available.split()]

fresh_count = 0
for a in available:
    for f in fresh:
        if f[0] <= a <= f[1]:
            fresh_count += 1
            break

print(fresh_count)