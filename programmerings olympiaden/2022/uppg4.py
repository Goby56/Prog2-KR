from typing import List, Tuple
N = int(input("N ? "))
FLOOR = [list(input(f"Rad {i+1} ? ")) for i in range(N)]

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
    return True

def generate_stroke_order(strokes_left: set, stroke_order: list):
    for color in "VS": 
        for stroke in strokes_left:

            strokes_left_copy = strokes_left.copy()
            stroke_order_copy = stroke_order.copy()

            strokes_left_copy.remove(stroke)
            stroke_order_copy.append((stroke, color))

            if len(strokes_left) == 1 and is_valid_order(stroke_order_copy):
                print(stroke_order_copy)
                return

            generate_stroke_order(strokes_left_copy, stroke_order_copy)


print(potential_strokes)
generate_stroke_order(potential_strokes, [])


        