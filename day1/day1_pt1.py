with open("day1_input.txt", "r") as f:
    data = f.readlines()

int_data = [int(item) for item in data] # cast array of strings to ints
increases = 0
for index, depth in enumerate(int_data):
    if int_data[index-1] < depth:
        increases+=1

print(increases)
