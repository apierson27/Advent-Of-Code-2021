from collections import Counter

with open("day2_input.txt", "r") as f:
    data = f.readlines()

dirs = {'forward': 0, 'up': 0, 'down': 0}
# Defining it here doesn't cause the values to update - suspect due to
# dict.update modifying in place?
main_counter = Counter(dirs)
for line in data:
    tmp = line.split()
    point = {tmp[0]:int(tmp[1])}
    # main_counter = Counter(dirs)
    tmp_counter = Counter(point)
    main_counter.update(tmp_counter)


x = main_counter['forward']
y = main_counter['down'] - main_counter['up']
print(f"Solution: {x*y}")
