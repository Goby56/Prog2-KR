import numpy as np
# grid = np.array([[int(y) for y in input().split()] for x in range(4)])
# move = int(input())
grid = np.array([
    [2, 0, 0, 2],
    [4, 16, 8, 2],
    [2, 64, 32, 4],
    [1024, 1024, 64, 0]
])
print(grid)
key = np.random.randint(0, 4)
print(key)
# 0, 1, 2, 3 = left, up, right, down
direction = 1 if key in [2, 3] else -1
print(direction)
if key in [1, 3]: # if the direction is vertical
    grid = np.transpose(grid) # flip rows and columns

def move(grid, r):
    for c in range(4)[::direction]:
        if grid[r][c] == 0: continue
        if grid[r][c + direction] == 0:
            grid[r][c + direction] = grid[r][c]
            grid[r][c] = 0

def combine(grid, r):
    for c in range(4)[::direction]:
        if grid[r][c] == 0: continue
        if grid[r][c + direction] != grid[r][c]: continue
        grid[r][c + direction] *= 2
        grid[r][c] = 0

for r in range(4):
    move(grid, r)
    combine(grid, r)
    move(grid, r)
    
    
# for c in range(4)[::-direction]:  
#     for i in range(c)[::direction]:
#         if grid[r][i] == 0: 
#             grid[r][i] = grid[r][i - direction]
#             grid[r][i - direction] = 0
#         if grid[r][i - direction] != grid[r][i]: break
#         grid[r][i] *= 2
#         grid[r][i - direction] = 0
#         break

# --------- Half good ---------
# for r in range(4):
#     for c in range(4)[::-direction]:  
#         for i in range(c)[::direction]:
#             if grid[r][i] == 0: 
#                 grid[r][i] = grid[r][i - direction]
#                 grid[r][i - direction] = 0
#             if grid[r][i - direction] != grid[r][i]: break
#             grid[r][i] *= 2
#             grid[r][i - direction] = 0
#             break

if key in [1, 3]:
    grid = np.transpose(grid)

print(grid)

