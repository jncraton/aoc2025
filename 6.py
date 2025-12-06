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

# Part 2

rows = [list(r.replace('\n','')) for r in open('6.txt').readlines()]

nums = []
op = None
total = 0
for col_idx in range(len(rows[0])):
    col = ""
    for row in rows:
        c = row[col_idx]

        if c == "+":
            op = sum
        elif c == "*":
            op = prod
        else:
            col += c

    if col.strip():
        nums.append(int(col))
    else: # Blank column, so do the math
        total += op([int(n) for n in nums])
        nums = []

total += op([int(n) for n in nums])
print(total)