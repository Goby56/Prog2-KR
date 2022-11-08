# https://projecteuler.net/problem=71

# *Using Stern-Brocot sequence (1,1,2,1,3,2,3,1,4,3,5,2,5,3,4,1,5)
d = 100
# TOOO SLOW
seq = [1, 1]
i = 0
while seq[len(seq)-2:] != [d-1, d]:
    seq.append(seq[i]+seq[i+1])
    if seq[len(seq)-2:] == [d-1, d]: break
    seq.append(seq[i+1])
    i += 1
    print(i)

fracs = []
for i in range(len(seq)-1):
    if seq[i]/seq[i+1] < 1 and seq[i+1] <= d:
        fracs.append((seq[i], seq[i+1]))

fracs = sorted(fracs, key=lambda f: f[0]/f[1])


for i, f in enumerate(fracs):
    if f == (3, 7):
        print(fracs[i-1][0])
        break


# sequence = stern_brocot(5)
# fractions = sorted([(sequence[i], sequence[i+1]) for i in range(len(sequence)-1) if sequence[i]/sequence[i+1] < 1 and sequence[i+1] <= 5])

# print(fractions)

        

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

# from json import load

# N = int(1e6)

# with open("primes.json", "r") as f:
#     PRIMES = load(f)

# def primes_under(n: int) -> list:
#     primes = []
#     for p in PRIMES:
#         if p > n:
#             break
#         primes.append(p)
#     return primes[::-1]

# def factors_of(n: int) -> list:
#     factors = [n] if n in PRIMES else []

#     for p in primes_under(n):
#         if n % p == 0:
#             if n // p != 1:
#                 factors.append(p)
#                 factors.extend(factors_of(n // p))
#             break
#     return factors

# def hcf(n, d):
#     common_denominators = []
#     d_factors = factors_of(d)

#     for fn in factors_of(n):
#         for i, fd in enumerate(d_factors):
#             if fn == fd:
#                 common_denominators.append(d_factors.pop(i))
#                 break

#     for factor in common_denominators:
#         n //= factor
#         d //= factor
#     return (n, d)

# def proper_fractions_under(n: int) -> list[tuple]:
#     proper_fractions = set()

#     for i in range(1, n+1):
#         for j in range(1, i):
#             fraction = hcf(j, i)
#             proper_fractions.add(fraction)
#             # if fraction not in proper_fractions:
#             #     proper_fractions.append(fraction)

#     return sorted(proper_fractions, key=lambda frac: frac[0]/frac[1])

# fractions = proper_fractions_under(1000)
# for i, frac in enumerate(fractions):
#     if frac == (3, 7):
#         print(fractions[i-1])
#         break


