

# n, q = [int(x) for x in input().split()]
# tests = [int(input()) for x in range(q)]

def sieve(n: int):
    numbers = [x for x in range(2, n)]
    # primes = [1 for x in range(n)]
    primes = []
    for m in numbers:
        primes.append(m)
        for i in range(m, n, m):
            print(i)
            numbers.remove(i)

    return primes


print(sieve(100))

