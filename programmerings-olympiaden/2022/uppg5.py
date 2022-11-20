from itertools import permutations, compress
word = list(input("Ord ? "))
vowels = "aeiouy"

def contains_short(word: list):
    if len(word) < 3: return False
    for i in range(len(word)-2):
        if word[i] in vowels and word[i+1] not in vowels and word[i+2] not in vowels:
            return True
    return False

n = 0

for m in range(len(word)):
    for p in set(permutations([0 if i > m else 1 for i in range(len(word))])):
        new_word = list(compress(word, p))
        if not contains_short(new_word):
            n += 1

print("Svar:", n)