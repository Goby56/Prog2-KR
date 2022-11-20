n_words = int(input("Antal ord ? "))
words = input("Mening ? ").split()

vowels = "aeiouy"

for nth_w, word in enumerate(words):
    short_vowels = []
    for i in range(len(word)-2):
        if word[i] in vowels and word[i+1] not in vowels and word[i+2] not in vowels:
            short_vowels.append(i)
    characters = list(word)
    for i in short_vowels[::-1]:
        characters.pop(i)
    words[nth_w] = "".join(characters[::-1])

print("Svar:", " ".join(words[::-1]))