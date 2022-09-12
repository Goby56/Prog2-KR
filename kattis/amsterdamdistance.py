from math import pi

M, N, R = [float(x) for x in input().split()]
ax, ay, bx, by = [int(x) for x in input().split()]


D = R * abs(ay - by) / N + R * min(ay, by) * pi * abs(ax - bx) / M 
print(D)