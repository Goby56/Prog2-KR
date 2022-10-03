from random import randint
import numpy as np

bounds = (20, 20)
margin = 0.1

x_min, y_min = int(bounds[0]*margin), int(bounds[1]*margin)
x_max, y_max = int(bounds[0]*(1-margin)), int(bounds[1]*(1-margin))
        

def generate_rectangle(min_size: int):
    x_0, y_0 = randint(x_min, x_max-min_size), randint(y_min, y_max-min_size)
    x_1, y_1 = randint(x_0+min_size, x_max), randint(y_0+min_size, y_max)

    shape = [[0 for x in range(bounds[0])] for y in range(bounds[1])]
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if y >= y_0 and y < y_1 and x >= x_0 and x < x_1:
                shape[y][x] = 1
    
    return shape

def generate_circle(min_size: int):
    radius = randint(min_size, int(min(bounds[0]*(1-margin*2), bounds[1]*(1-margin*2))/2))
    x_0, y_0 = randint(x_min+radius, x_max-radius), randint(y_min+radius, y_max-radius)

    shape = [[0 for x in range(bounds[0])] for y in range(bounds[1])]
    for y in range(bounds[1]):
        for x in range(bounds[0]):
            if (y_0 - y)**2 + (x - x_0)**2 < radius**2:
                shape[y][x] = 1
    
    return shape


weights = [[0 for x in range(bounds[0])] for y in range(bounds[1])]
bias = 1000

for i in range(100):
    shape_type = randint(0, 1)
    input_pattern = generate_rectangle(7) if shape_type else generate_circle(4)

    total = 0
    for r in range(bounds[1]):
        for c in range(bounds[0]):
            total += input_pattern[r][c] * weights[r][c]

    for r in range(bounds[1]):
        for c in range(bounds[0]):      
            if total > bias and shape_type == 1:
                weights[r][c] += input_pattern[r][c]
            else: 
                weights[r][c] -= input_pattern[r][c]

print(np.array(weights))

        