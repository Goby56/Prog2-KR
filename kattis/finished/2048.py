grid = [[int(y) for y in input().split()] for x in range(4)]
direction = int(input())
# 0, 1, 2, 3 = left, up, right, down

def rotate_matrix(m):
    # copy pasta
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

for i in range(direction):
    grid = rotate_matrix(grid)

def combine(r):
    for c in range(3):
        if grid[r][c] == 0: continue
        if grid[r][c + 1] != grid[r][c]: continue
        grid[r][c] *= 2
        grid[r][c + 1] = 0

def move(r):
    for c in range(4):
        for i in range(c)[::-1]:
            if grid[r][i] == 0:
                grid[r][i] = grid[r][i + 1]
                grid[r][i + 1] = 0

for r in range(4):
    move(r)
    combine(r)
    move(r)

for i in range(4 - direction):
    grid = rotate_matrix(grid)

for row in grid:
    print(*row)