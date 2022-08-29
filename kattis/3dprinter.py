# https://open.kattis.com/problems/3dprinter

days = 0
printers = 1
statues = 0
goal = int(input())

while statues < goal:
    if printers < goal-statues:
        printers *= 2
    else:
        statues += printers

    days += 1

print(days)

# goal = int(input())
# statues = 0
# printers = 1
# day = 0
# while statues < goal:
#     if day < goal // 2:
#         printers *= 2
#     else:
#         statues += printers
#     day += 1
# print(day)
