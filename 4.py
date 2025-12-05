grid = [list(row.strip()) for row in open('4-1.txt').readlines()]

print(grid)

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


print(adj(grid, 1,1))