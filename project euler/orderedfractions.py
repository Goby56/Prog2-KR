# https://projecteuler.net/problem=71

fractions = []


def factors(n):
    # find all factors of n
    # test 0-9 and all primes up to 10^6
    pass


def hcf(n, d):
    
    pass


for d in range(int(1e6)):
    for n in range(d):
        if hcf(n, d):
            fractions.append((n, d))
