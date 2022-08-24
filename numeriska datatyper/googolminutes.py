import time

t = int(time.time()) + (10**100)*60 + 3600 * 2

t %= 3600*24  # Seconds past on that day

hours = t // 3600  # Hour that day
minutes = int(((t % 3600)/3600)*60)  # Minutes that hour

print(f"{hours}:{minutes}")
