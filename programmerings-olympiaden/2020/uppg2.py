with open("uppg2.txt", "r") as f:
    K, N, *x = [int(x.split()[-1]) for x in f.readlines()]

c = 0 # Number of cans
while N > 0:
    for i, b in enumerate(x): # bag
        if b == max(x):
            if b >= 10:
                N -= 10
                x[i] -= 10
            else:
                N -= b
                x[i] = 0
            break
    print(x)
    c += 1

print("Svar:", c)