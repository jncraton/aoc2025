from math import prod

problems = list(zip(*[r.split() for r in open('6.txt').readlines()]))

total = 0

for problem in problems:
    op = problem[-1]
    operands = [int(p) for p in problem[:-1]]

    if op == "+":
        total += sum(operands)
    if op == "*":
        total += prod(operands)

print(total)