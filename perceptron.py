from random import randint


        

def generate_rectangle(bounds: tuple, margin: float, min_size: int):

    x_min, y_min = int(bounds[0]*margin), int(bounds[1]*margin)
    x_max, y_max = int(bounds[0]*(1-margin)), int(bounds[1]*(1-margin))

    x_0, y_0 = randint(x_min, x_max-min_size), randint(y_min, y_max-min_size)
    