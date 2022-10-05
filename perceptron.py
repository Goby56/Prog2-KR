from random import randint
import numpy as np

bounds = (20, 20)
margin = 0.1

class Perceptron:
    def __init__(self, bounds: tuple, bias: float, min_radius = 0.1, min_size = 0.2) -> None:
        self.weights = np.zeros(bounds)
        self.bounds = bounds
        self.bias = bias
        
        self.x_min, self.y_min = int(bounds[0]*margin), int(bounds[1]*margin)
        self.x_max, self.y_max = int(bounds[0]*(1-margin)), int(bounds[1]*(1-margin))

        self.min_radius, self.min_size = min_radius, min_size

    def predict(self, input_pattern: np.ndarray):
        total = np.dot(input_pattern.flatten(), self.weights.flatten())

        return 1 if total > self.bias else 0 # Circle = 1, rectangle = 0

    def train(self, iterations: int):
        for i in range(iterations):
            shape_type = randint(0, 1) # rectangle, circle
            input_pattern = self.generate_circle() if shape_type else self.generate_rectangle()

            total = np.dot(input_pattern.flatten(), self.weights.flatten())

            # for r in range(bounds[1]):
            #     for c in range(bounds[0]):
            #         total += input_pattern[r][c] * weights[r][c]

            if total < self.bias and shape_type == 1:
                self.weights = np.add(self.weights, input_pattern)
            elif total > self.bias and shape_type == 0:
                self.weights = np.subtract(self.weights, input_pattern)
            
            # for r in range(bounds[1]):
            #     for c in range(bounds[0]):      
            #         if total < bias and shape_type == 1:
            #             weights[r][c] += input_pattern[r][c]
            #         elif total > bias and shape_type == 0:
            #             weights[r][c] -= input_pattern[r][c]

    def generate_rectangle(self):
        min_size_x, min_size_y = int(bounds[0] * self.min_size), int(bounds[1] * self.min_size)
        x_0, y_0 = randint(self.x_min, self.x_max-min_size_x), randint(self.y_min, self.y_max-min_size_y)
        x_1, y_1 = randint(x_0+min_size_x, self.x_max), randint(y_0+min_size_y, self.y_max)

        shape = np.zeros(self.bounds)
        
        for y in range(bounds[1]):
            for x in range(bounds[0]):
                if y >= y_0 and y < y_1 and x >= x_0 and x < x_1:
                    shape[y][x] = 1
        
        return shape

    def generate_circle(self):
        min_radius = int(min(bounds) * self.min_radius)
        radius = randint(min_radius, int(min(bounds[0]*(1-margin*2), bounds[1]*(1-margin*2))/2))
        x_0, y_0 = randint(self.x_min+radius, self.x_max-radius), randint(self.y_min+radius, self.y_max-radius)

        shape = np.zeros(self.bounds)

        for y in range(bounds[1]):
            for x in range(bounds[0]):
                if (y_0 - y)**2 + (x - x_0)**2 < radius**2:
                    shape[y][x] = 1
        
        return shape

circles = 0
for i in range(100):
    model = Perceptron((20,20), 100)
    model.train(100)
    circles += model.predict(np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]))

print(1-circles/100)

model = Perceptron((20,20), 100)
model.train(100)
print(model.weights)

        