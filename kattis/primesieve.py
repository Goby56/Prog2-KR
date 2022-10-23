n, q = [int(x) for x in input().split()]
# tests = [int(input()) for x in range(q)]

def primes_under(n: int):
    numbers = range(2, n+1)
    primes = [True for x in range(2, n+1)]

    for i, m in enumerate(numbers):
        # numbers[i] is prime but every multiple numbers[i+m] is not
        for k in range(i+m, n-1, m):
            primes[k] = False
    return sum(primes)

def is_prime(n: int):
    if n == 1:
        return 0
    for m in range(2, n):
        if n % m == 0:
            return 0
    return 1

print(primes_under(n))

for i in range(q):
    print(is_prime(int(input())))


"""
9973 6
1
2
3
4
9972
9973
"""

# -------- Memory hog --------
def sieve(n: int):
    numbers = [x for x in range(2, n+1)]
    primes = [1 for x in range(n)]

    for i, m in enumerate(numbers):
        for k in range(i+m, n, m):
            primes[k] = 0

    return [x for i, x in enumerate(numbers) if primes[i] == 1]
