ranges = open("2.txt").read().split(",")

total = 0

for r in ranges:
    start, stop = map(int, r.split('-'))

    for i in range(start, stop+1):
        i = str(i)

        if len(i) % 2 == 0:
            l = i[:len(i)//2]
            r = i[len(i)//2:]
            if l == r:
                total += int(i)

print(total)