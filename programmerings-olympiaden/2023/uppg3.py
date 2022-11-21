# N = int(input("N ? "))
# rooms = [(int(input(f"Omr {i+1}, vån ? ")), input(f"Omr {i+1}, tr  ? ")) for i in range(N)]
from typing import Tuple
with open("uppg3.txt", "r") as f:
    N = int(f.readline())
    rooms = [(int(f.readline().strip("\n")), f.readline().strip("\n")) for _ in range(N)]

print(N)
print(list(rooms))

distances = dict()

def explore(previous_room: int, room_index: int, path_length: int):
    current_room = rooms[room_index]
    
    for i, r in enumerate(rooms):
        if i == room_index or i == previous_room: continue
        possible_rooms = []
        for s in r[1]:
            if s in current_room[1]:
                possible_rooms.append(i)
        if len(possible_rooms) == 0: continue
        shortest_dist = 101
        j = -1
        for k in possible_rooms:
            dist = abs(current_room[0] - rooms[k][0])
            if dist < shortest_dist:
                j = k
                shortest_dist = dist
        
        dist = path_length + abs(current_room[0] - rooms[j][0])
        print(room_index + 1, j + 1)
        if j == room_index + 1:
            distances[str(room_index)+str(j)] = dist
            return
        explore(room_index, j, dist)

explore(0, 0, 0)

print(distances)





