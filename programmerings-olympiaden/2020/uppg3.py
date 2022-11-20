from itertools import product
import time

with open("uppg3.txt", "r") as f:
    N, K, M = [int(f.readline().split()[-1]) for _ in range(3)]
    groups = [f.readline().split()[-1] for _ in range(M)]

species = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:K]

combinations = 0

def is_valid_neighbors(a: str, b: str):
    for g in groups:
        if a in g and b in g or a == b: return False
    return True

def num_of_config(a: str, i: int):
    global combinations
    if i == 0:
        print(combinations)
        combinations += 1
        return
    for s in species:
        if is_valid_neighbors(a, s):
            num_of_config(s, i-1)

if M == 0:
    combinations = K*(K-1)**(N-1)
else:
    for a in species:
        num_of_config(a, N-1)

print(combinations)

# def is_valid(animals: tuple):
#     for i in range(N-1):
#         for g in groups:
#             if animals[i] in g and animals[i+1] in g or animals[i] == animals[i+1]: return False
#     return animals


# combinations = filter(is_valid, product(species, repeat=N))

# print("Svar:", len(list(combinations)))