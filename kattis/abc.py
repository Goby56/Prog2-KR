abc = sorted([int(x) for x in input().split(" ")])
order = input()

print(*[abc[{"A": 0, "B": 1, "C": 2}[i]] for i in order])