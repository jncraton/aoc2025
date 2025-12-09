import sys
from itertools import combinations

sys.setrecursionlimit(100000)

reds = [[int(v) for v in l.strip().split(",")] for l in open("9.txt").readlines()]

rects = []

for a, b in combinations(reds, 2):
    area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
    rects.append(tuple([area, a, b]))

rects.sort()

print(rects[-1][0])

# Part 2
#
# 1. Create bounds set
# 2. Iterate largest rects until we find one who contains all green

bounds = set()

for a, b in zip(reds, reds[1:] + reds[:1]):
    if a[0] == b[0]:
        start = min(a[1], b[1])
        end = max(a[1], b[1]) + 1
        for y in range(start, end):
            bounds.add((a[0], y))
    if a[1] == b[1]:
        start = min(a[0], b[0])
        end = max(a[0], b[0]) + 1
        for x in range(start, end):
            bounds.add((x, a[1]))


def is_inside(bounds, point):
    """Ray-casting interior check"""
    if point in bounds:
        return True

    x, y = point

    bounds_crossed = 0

    # Due to integer precision, we have to keep track of when we are above or below a line within its cell
    above = False
    below = False

    in_bound = False
    for i in range(0, x + 1):
        if (i, y) not in bounds and in_bound:
            # We've just left a bound
            # We still have to confirm we weren't riding a bound
            if above and (i - 1, y - 1) in bounds and (i - 1, y + 1) not in bounds:
                pass
            elif below and (i - 1, y + 1) in bounds and (i - 1, y - 1) not in bounds:
                pass
            else:
                bounds_crossed += 1
            in_bound = False
            above = False
            below = False

        if (i, y) in bounds and not in_bound:
            # Entering a bound
            in_bound = True

            # If we enter at a corner, not whether we are now above or below the bound
            if (i, y - 1) in bounds and (i, y + 1) not in bounds:
                above = True
            if (i, y + 1) in bounds and (i, y - 1) not in bounds:
                below = True

    return bounds_crossed % 2 == 1


if False:
    import pandas as pd
    import matplotlib.pyplot as plt

    # pd.DataFrame(bounds).plot.scatter(0, 1)
    # plt.show()

    greens = []
    for x in range(0, 15):
        for y in range(0, 15):
            if is_inside(bounds, (x, y)):
                greens.append((x, y))

    pd.DataFrame(greens).plot.scatter(0, 1)
    plt.show()


def is_valid(rect, bounds):
    """Confirm that all points are within bounds"""

    # Rule out corners first
    if not is_inside(bounds, (rect[1][0], rect[1][1])):
        return False
    if not is_inside(bounds, (rect[2][0], rect[2][1])):
        return False
    if not is_inside(bounds, (rect[1][0], rect[2][1])):
        return False
    if not is_inside(bounds, (rect[2][0], rect[1][1])):
        return False

    for x in [min(rect[1][0], rect[2][0]), max(rect[1][0], rect[2][0])]:
        print(f"{x=}")
        for y in range(min(rect[1][1], rect[2][1]), max(rect[1][1], rect[2][1]) + 1):
            if not is_inside(bounds, (x, y)):
                return False

    for y in [min(rect[1][1], rect[2][1]), max(rect[1][1], rect[2][1])]:
        print(f"{y=}")
        for x in range(min(rect[1][0], rect[2][0]), max(rect[1][0], rect[2][0]) + 1):
            if not is_inside(bounds, (x, y)):
                return False

    return True


for rect in rects[::-1]:
    print(rect)
    if is_valid(rect, bounds):
        print(rect[0])
        break
