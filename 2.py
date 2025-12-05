ranges = open("2.txt").read().split(",")

total = 0

for r in ranges:
    start, stop = map(int, r.split('-'))

    for i in range(start, stop+1):
        i = str(i)

        for step in range(1, (len(i)//2)+1):
            if len(i) % step == 0:
                for idx in range(0, len(i)-step, step):
                    l = i[idx:idx+step]
                    r = i[idx+step:idx+step+step]
                    if l != r:
                        break
                else:
                    total += int(i)
                    break

print(total)