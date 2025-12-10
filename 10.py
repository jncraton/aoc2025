import re
from queue import PriorityQueue

machines = []

for line in open('10-1.txt').readlines():
    machines.append({
        "goal": tuple(b == '#' for b in re.search(r'\[(.*?)\]', line)[1]),
        "edges": [tuple(int(n) for n in e.split(',')) for e in re.findall(r'\((.*?)\)', line)],
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

# This is BFS over the button combos

total = 0
iters = 0

for i, machine in enumerate(machines):
    print(f"{i}/{len(machines)}: {machine['joltage_goal']} {machine['edges']}")
    frontier = PriorityQueue()
    start = tuple([0] * len(machine['joltage_goal']))
    visited = set()
    visited.add(start)
    for edge in machine['edges']:
        frontier.put((0, 0, start, edge))

    best_press = max(len(e) for e in machine['edges'])

    last_heuristic = 0
    while True:
        iters+=1
        heuristic, cost, state, edge = frontier.get()

        if state == machine['joltage_goal']:
            total += cost
            break

        cost += 1

        if any(cur > goal for cur, goal in zip(state, machine['joltage_goal'])):
            continue

        distance = sum(goal - cur for cur, goal in zip(state, machine['joltage_goal']))

        heuristic = cost + distance / best_press

        if heuristic > last_heuristic:
            print(i, heuristic, distance, cost, state, edge)
            last_heuristic = heuristic

        for edge in machine['edges']:
            next_state = tuple(j+1 if i in edge else j for i, j in enumerate(state))

            if next_state not in visited:
                visited.add(next_state)
                frontier.put((heuristic, cost, next_state, edge))

print("Total iterations:", iters)
print(total)
