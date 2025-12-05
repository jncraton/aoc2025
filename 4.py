grid = [list(row.strip()) for row in open('4-1.txt').readlines()]

print(grid)

def get(grid, x, y):
    if x < 0 or y < 0:
        return None

    try:
        return grid[y][x]
    except IndexError:
        return None

print(get(grid, 100, 100))