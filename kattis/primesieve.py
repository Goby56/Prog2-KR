# n, q = [int(x) for x in input().split()]
# tests = [int(input()) for x in range(q)]

def primes_under(n: int):
    numbers = range(2, n+1)

    n_primes = n

    for i, m in enumerate(numbers):
        for k in range(i+m, n, m):
            n_primes -= 1

    return n_primes


# print(len(primes))

# for i in range(q):
#     number = int(input())
#     print(1) if number in primes else print(0)


def sieve(n: int):
    numbers = [x for x in range(2, n+1)]
    primes = [1 for x in range(n)]
    
    for i, m in enumerate(numbers):
        for k in range(i+m, n, m):
            primes[k] = 0

    return [x for i, x in enumerate(numbers) if primes[i] == 1]

print(len(sieve(101)))
print(primes_under(101))


