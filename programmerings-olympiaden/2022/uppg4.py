from typing import List, Tuple
from itertools import permutations, combinations_with_replacement, combinations, product
import time
import numpy as np
from PIL import Image
# N = int(input("N ? "))
# FLOOR = [list(input(f"Rad {i+1} ? ")) for i in range(N)]

# N = 4
# FLOOR = [
#     [".",".","S","."],
#     ["V","V","S","V"],
#     [".",".","S","."],
#     [".",".","S","."]
# ]

# N = 5
# FLOOR = [
#     ["V","V","V","V","V"],
#     [".",".","S",".","S"],
#     ["V","V","V","V","S"],
#     ["V","V","V","V","V"],
#     [".",".","S",".","S"]
# ]

N = 6
FLOOR = [
    ["V","V","V","V","V","V"],
    ["V","V","V","S","V","V"],
    ["V","V","V","S","V","V"],
    ["V",".","V","S","V","."],
    ["S","S","S","S","S","S"],
    ["V",".","V","S","V","."]
]

numbers = "123456789"[0:N]
letters = "ABCDEFGHI"[0:N]

unpainted_files = set()
filled_files = set()

def is_completely_filled(file: list):
    n = len(file)
    for i in range(n):
        if file[i] != file[(i+1)%n]:
            return False
    return True


for r in range(N):
    row = []
    column = []

    for c in range(N):
        if FLOOR[r][c] == ".":
            unpainted_files.add(numbers[r])
            unpainted_files.add(letters[c])
        row.append(FLOOR[r][c])
        column.append(FLOOR[c][r])
    
    if is_completely_filled(row):
        filled_files.add((numbers[r], row[0]))
    if is_completely_filled(column):
        filled_files.add((letters[r], column[0]))
   
potential_strokes = set(numbers).union(set(letters)).difference(unpainted_files, map(lambda x: x[0], filled_files))

def is_valid_order(stroke_order: List[Tuple[str, str]]):
    pattern = [["." for c in range(N)] for r in range(N)]
    for s in stroke_order:
        for n in range(N):
            if s[0].isdigit():
                file_index = numbers.index(s[0])
                pattern[file_index][n] = s[1]
            else:
                file_index = letters.index(s[0])
                pattern[n][file_index] = s[1]
    for r in range(N):
        for c in range(N):
            if pattern[r][c] != FLOOR[r][c]:
                return False
    print(stroke_order)
    return True

def generate_order(undetermined_strokes: set[str], final_strokes: set[Tuple[str, str]]):    
    for file_order in permutations(undetermined_strokes):
        for color_order in product("VS", repeat=len(undetermined_strokes)):
            stroke_order = list(zip(file_order, color_order))
            stroke_order.extend(final_strokes)
            if is_valid_order(stroke_order):
                print("Ordning:", "".join(map(lambda x: x[0], stroke_order)))
                print("Färger :", "".join(map(lambda x: x[1], stroke_order)))
                yield stroke_order

def create_image(stroke_order: List[Tuple[str, str]]):
    pattern = np.full((N,N), 0.5)
    for s in stroke_order:
        if s[0].isdigit():
            pattern[:,numbers.index(s[0])] = 1 if s[1] == "V" else 0
        else:
            pattern[letters.index(s[0]),:] = 1 if s[1] == "V" else 0
    return pattern

stroke_orders = generate_order(potential_strokes, filled_files)

print(create_image(next(stroke_orders)))


# color_options = ["V" for _ in range(len(potential_strokes))]
# color_options.extend(["S" for _ in range(len(potential_strokes))])

# t0 = time.time()
# perm = set(permutations(color_options, len(potential_strokes)))

# print(time.time() - t0)