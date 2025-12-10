import re
from queue import PriorityQueue

machines = []

for line in open('10-1.txt').readlines():
    machines.append({
        "goal": tuple(b == '#' for b in re.search(r'\[(.*?)\]', line)[1]),
        "edges": [tuple(int(n) for n in e.split(',')) for e in re.findall(r'\((.*?)\)', line)],
        "weights": tuple(int(n) for n in re.search(r'\{(.*?)\}', line)[1].split(',')),
    })

# This is BFS over the button combos

total = 0

for machine in machines:
    visited = set()
    frontier = PriorityQueue()
    start = tuple([False] * len(machine['goal']))
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
            print(cost, state, edge)
            break

        for edge in machine['edges']:
            frontier.put((cost, state, edge))

print(total)      
