n = int(input())
integers = [int(input()) for x in range(n)]
integers.reverse()
for x in integers:
    print(x)