from collections import Counter

with open("day2_input.txt", "r") as f:
    data = f.readlines()

dirs = Counter({'forward': 0, 'up': 0, 'down': 0})
for line in data:
    tmp = line.split()
    point = {tmp[0]:int(tmp[1])}
    dirs.update(point)

x = dirs['forward']
y = dirs['down'] - dirs['up']
print(f"Solution: {x*y}")
