N = int(input("Antal med grönt kort, N  ? "))
M = int(input("Antal utan grönt kort, M ? "))

minutes = 0

if M == 0:
    minutes += 20 if N % 2 == 0 else 30
elif M < N:
    minutes += 20 if N % 2 == 0 else 30
elif M == N:
    minutes += 30
elif M > N:
    minutes += 10*(M//N) + 10*(M % N)
    minutes += 20

print("Svar:", minutes)


"""
Test
N = 3, (A,B,C)
M = 1, (D)

AD, BC
AB
BA

10min: NM, NN
10min: NN
10min: NN 

N = 2, (A,B)
M = 3, (C,D,E)

AC, BD
AE
AB
BA

10min: NM, NM
10min: NN
10min: NN
10min: NM

N = 6, (A,B,C,D,E,F)
M = 2, (G,H)

AG, BH, CD, EF
AB, DC, FE
BA

N = 5 (A,B,C,D,E)
M = 7 (F,G,H,I,J,K,L)

AF, BG, CH, DI, EJ
AK, BL, CD
AE, BC
CA, DB

N = 5 (A,B,C,D,E)
AB, CD
AE, BC
BA
(5,2) = 10

N = 6 (A,B,C,D,E,F)
AB, CD, EF
BA, DC, FE
(6,2) = 15

N = 7 (A,B,C,D,E,F,G)
AB, CD, EF
BA, DC, FE
AG
(7,2) = 21

N = 8 (A,B,C,D,E,F,G,H)
AB, CD, EF, GH
BA, DC, FE, HG
(8,2) = 28

ABC
DEF

Ad, BC
AB, Ce
BA, Cf

AB, Cd

AB
cdef

Ac, Bd
Ae, Bf
AB
BA

ABCD
efgh

Ae, Bf, Cg, Dh
AB, CD
BA, DC

ABC
ef

Ae, Bf
A

ABCDE
fghij

AB, CD, Ef
BA, DC, Eg
Ah, Bi, Cj, De

ABCDE
fghi

AB, Cf, Dg, Eh
Ai, BC, DE
BA, ED,





"""
