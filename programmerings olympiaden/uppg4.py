import numpy as np
from PIL import Image

rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
N = int(input("N ? "))
floor = [list(input(f"Rad {n} ")) for n in range(1, N+1)]

valid_rows, valid_columns = rows, columns

for r in range(N):
    for c in range(N):
        if floor[r][c] == ".":
            valid_rows[r], valid_columns[c] = 0, 0

valid_rows = [x for x in valid_rows if x != 0]
valid_columns = [x for x in valid_columns if x != 0]
valid_instructions = valid_rows.extend(valid_columns)


def get_configuration(valid_inst: list, prev_inst: list):
    # if paint with prev_inst is the desired pattern print and program
    for inst in valid_inst:
        out_inst = prev_inst.copy()
        out_inst.append(inst)
        get_configuration(out_inst)



# colors = {"V": 255, ".": 127, "S": 0}

# N = int(input("N ? "))
# wall = np.array([list(map(lambda x: colors[x], list(
#     input(f"Rad {n} ")))) for n in range(1, N+1)])


# Image.fromarray(wall).resize((1000, 1000), resample=Image.BOX).show()
