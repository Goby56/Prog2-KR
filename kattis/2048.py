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
# move = np.random.randint(0, 4)
move = 0

# 0, 1, 2, 3 = left, up, right, down
direction = 1 if move in [2, 3] else -1


# if move in [0, 2]:
#     for r in range(4):
#         while True:
#             for c in range(4)[::direction]:
#                 if grid[r][c + direction] == 0:
#                     grid[r][c + direction] = grid[r][c]
#                     grid[r][c] = 0
#                     continue
#                 if grid[r][c] != grid[r][c + direction]:
#                     break
#                 grid[r][c + direction] *= 2
#                 grid[r][c] = 0


if move in [0, 2]:
    for r in range(4):
        for c in range(4)[::-direction]:  
            for i in range(c)[::direction]:
                if grid[r][i] == 0: 
                    j = i
                    while grid[r][j] != 0:
                        pass
                    # keep checking if it is zero
                    grid[r][i] = grid[r][c]
                    grid[r][c] = 0
                    continue
                if grid[r][c] != grid[r][i]: break
                grid[r][i] *= 2
                grid[r][c] = 0

print(grid)

