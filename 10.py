import re
from queue import PriorityQueue

machines = []

for line in open('10-1.txt').readlines():
    machines.append({
        "goal": tuple(b == '#' for b in re.search(r'\[(.*?)\]', line)[1]),
        "edges": sorted([tuple(int(n) for n in e.split(',')) for e in re.findall(r'\((.*?)\)', line)], key=lambda e: -len(e)),
        "joltage_goal": tuple(int(n) for n in re.search(r'\{(.*?)\}', line)[1].split(',')),
    })

# This is BFS over the button combos

total = 0

for machine in machines:
    frontier = PriorityQueue()
    start = tuple([False] * len(machine['goal']))
    visited = set()
    visited.add(start)
    for edge in machine['edges']:
        frontier.put((0, start, edge))

    while True:
        cost, state, edge = frontier.get()

        cost += 1

        state = tuple(not s if i in edge else s for i, s in enumerate(state))

        if state in visited:
            continue

        visited.add(state)

        if state == machine['goal']:
            total += cost
            break

        for edge in machine['edges']:
            frontier.put((cost, state, edge))

print(total)      

# Part 2
#
# We need a different approach here
#
# The output should be a linear combination of the buttons
#
# For the first machine:
#
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
#
# Labelling the buttons:
#
# [.##.] a(3) b(1,3) c(2) d(2,3) e(0,2) f(0,1) {3,5,4,7}
# 3 = e
# 5 = b
# 4 = c + d + e
# 7 = a + b + d
#
# We can solve this easily enough:
#
# e = 3
# b = 5
# 
