grid = [list(row.strip()) for row in open('4.txt').readlines()]

def get(grid, x, y):
    if x < 0 or y < 0:
        return None

    try:
        return grid[y][x]
    except IndexError:
        return None

def adj(grid, x, y):
    res = []

    for i in [x-1, x, x+1]:
        for j in [y-1, y, y+1]:
            if i != x or j != y:
                if get(grid, i, j):
                    res.append((i, j, get(grid, i, j)))

    return res

def remove_pass(grid):
    total = 0
    for row,row_content in enumerate(grid):
        for col,_ in enumerate(row_content):
            if get(grid, col, row) != '@':
                continue
            
            rolls = [g for g in adj(grid, col, row) if g[2] == '@']
            if len(rolls) < 4:
                total += 1
                grid[row][col] = ''

    return total

total = 0
while removed := remove_pass(grid):
    total += removed

print(total)