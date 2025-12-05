grid = [list(row.strip()) for row in open('4-1.txt').readlines()]

print(grid)

def get(grid, x, y):
    return grid[y][x]

print(get(grid, -1, -1))