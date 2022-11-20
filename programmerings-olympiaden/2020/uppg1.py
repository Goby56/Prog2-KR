with open("uppg1.txt", "r") as f:
    n = int(f.readline())
p = [0,1] # Previous
i = 0
while n > 0:
    l = sum(p) # Lost
    n -= p[1]
    p[0] = p[1]
    p[1] = l
    i += 1
print(i)

