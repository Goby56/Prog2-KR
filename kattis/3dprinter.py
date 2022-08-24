# https://open.kattis.com/problems/3dprinter

# days = 0
# printers = 1
# statues = 0
# goal = 10

# while statues < goal:
#     for p in range(printers):
#         pass

#     days += 1

goal = int(input())
statues = 0
printers = 1
day = 0
while statues < goal:
    if day < goal // 2:
        printers *= 2
    else:
        statues += printers
    day += 1
print(day)
