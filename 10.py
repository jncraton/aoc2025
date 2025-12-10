import re

machines = []

for line in open('10-1.txt').readlines():
    machines.append({
        "goal": tuple(b == '#' for b in re.search(r'\[(.*?)\]', line)[1]),
        "edges": [tuple(int(n) for n in e.split(',')) for e in re.findall(r'\((.*?)\)', line)],
        "weights": tuple(int(n) for n in re.search(r'\{(.*?)\}', line)[1].split(',')),
    })

# This is BFS over the button combos
