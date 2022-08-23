c = int(input())

percentage_average = [] # length of c

for i in range(c):
    case = input().split(" ")
    
    n = int(case[0])
    grades = [int(x) for x in case[1:]] # length of n
    
    mean = sum(grades) / n
    
    above_average = 0
    for s in range(n):
        if grades[s] > mean:
            above_average += 1
            
    percentage_average.append(above_average / n)

for p in percentage_average:
    percentage = '{0:.3f}'.format(p * 100)
    print(f"{percentage}%")
