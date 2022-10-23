# https://open.kattis.com/problems/amsterdamdistance?editsubmit=9374129

from math import pi

M, N, R = [float(x) for x in input().split()]
ax, ay, bx, by = [int(x) for x in input().split()]

angle = pi * (abs(ax - bx) / M) # The angle between the two streets

arc_len = R * (min(ay, by) / N) * angle # The length of the shortest arc
straight_len = 2 * R * min(ay, by) / N # The length of the straight inner path from each point of the shortest arc

diff_len = R * abs(ay - by) / N # The length from canal A to canal B

print(min(arc_len, straight_len) + diff_len)
print("arc") if arc_len < straight_len else print("straight")