from collections import Counter

with open("day2_input.txt", "r") as f:
    data = f.readlines()

dirs = Counter({'forward': 0, 'depth': 0})
aim = 0
for line in data:
    tmp = line.split()
    point = {tmp[0]:int(tmp[1])}
    if 'down' in point.keys():
        aim += point['down']
    if 'up' in point.keys():
        aim -= point['up']
    if 'forward' in point.keys():
        forward_move = point['forward']
        total_move = {'forward': forward_move, 'depth': aim*forward_move}
        dirs.update(total_move)


print(f"Solution: {dirs['forward']*dirs['depth']}")
