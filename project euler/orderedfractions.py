# https://projecteuler.net/problem=71

N = int(1e3)

def find_primes_under(n) -> list:
    primes = []

    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(n: int) -> bool:
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


PRIMES = find_primes_under(N)


def primes_under(n: int) -> list:
    primes = []
    for p in PRIMES:
        if p > n:
            return primes[::-1]
        primes.append(p)
    return primes[::-1]


def factors_of(n: int) -> list:
    factors = [n] if is_prime(n) else []

    for p in primes_under(n):
        if n % p == 0:
            if n // p != 1:
                factors.append(p)
                factors.extend(factors_of(n // p))
            break
    return factors


print(factors_of(N))


def hcf(n, d):
    common_denominators = []
    for i in factors_of(n):
        for j in factors_of(d):
            if i == j:
                common_denominators.append(i)
    print(common_denominators)

    
def proper_fractions_under(n: int) -> list:
    proper_fractions = []

    for d in range(n):
        for n in range(d):
            if hcf(n, d):
                proper_fractions.append((n, d))
    return proper_fractions


hcf(40, 80)
