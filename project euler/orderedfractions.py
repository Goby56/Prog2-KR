# https://projecteuler.net/problem=71

# def find_primes_under(n) -> list:
#     primes = []

#     for i in range(2, n):
#         if is_prime(i):
#             primes.append(i)
#     return primes


# def is_prime(n: int) -> bool:
#     for d in range(2, n):
#         if n % d == 0:
#             return False
#     return True

# PRIMES = find_primes_under(N)

from json import load

N = int(1e6)

with open("primes.json", "r") as f:
    PRIMES = load(f)

def primes_under(n: int) -> list:
    primes = []
    for p in PRIMES:
        if p > n:
            break
        primes.append(p)
    return primes[::-1]

def factors_of(n: int) -> list:
    factors = [n] if n in PRIMES else []

    for p in primes_under(n):
        if n % p == 0:
            if n // p != 1:
                factors.append(p)
                factors.extend(factors_of(n // p))
            break
    return factors

def hcf(n, d):
    common_denominators = []
    d_factors = factors_of(d)

    for fn in factors_of(n):
        for i, fd in enumerate(d_factors):
            if fn == fd:
                common_denominators.append(d_factors.pop(i))
                break

    for factor in common_denominators:
        n //= factor
        d //= factor
    return (n, d)

def proper_fractions_under(n: int) -> list[tuple]:
    proper_fractions = set()

    for i in range(1, n+1):
        for j in range(1, i):
            fraction = hcf(j, i)
            proper_fractions.add(fraction)
            # if fraction not in proper_fractions:
            #     proper_fractions.append(fraction)

    return sorted(proper_fractions, key=lambda frac: frac[0]/frac[1])

fractions = proper_fractions_under(1000)
for i, frac in enumerate(fractions):
    if frac == (3, 7):
        print(fractions[i-1])
        break


