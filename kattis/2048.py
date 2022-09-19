import numpy as np
# grid = np.array([[int(y) for y in input().split()] for x in range(4)])
# move = int(input())
grid = np.array([
    [2, 0, 0, 2],
    [4, 16, 8, 2],
    [2, 64, 32, 4],
    [1024, 1024, 64, 0]
])
# grid = np.array([
#     [16, 0, 0, 32],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [64, 0, 0, 4]
# ])
print(grid)
key = np.random.randint(0, 4)
print(key)
# 0, 1, 2, 3 = left, up, right, down

grid = np.rot90(grid, key)

# def combine(grid, r):
#     for c in range(4)[::direction]:
#         if grid[r][c] == 0: continue
#         if grid[r][c + direction] != grid[r][c]: continue
#         grid[r][c + direction] *= 2
#         grid[r][c] = 0


def combine(r):
    pass


def move(r):
    for c in range(4):
        for i in range(c)[::-1]:
            if grid[r][i] == 0:
                grid[r][i] = grid[r][i + 1]
                grid[r][i + 1] = 0


for r in range(4):
    move(r)
    # implement combine function

grid = np.rot90(grid, -key)

print(grid)
