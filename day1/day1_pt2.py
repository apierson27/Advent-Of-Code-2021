with open("day1_input.txt", "r") as f:
    data = f.readlines()

int_data = [int(item) for item in data]
increases = 0
index = 0
while index < len(int_data):
    # break if < 3 values left
    if len(int_data[index+1:index+4]) < 3:
        break
    if sum(int_data[index:index+3]) < sum(int_data[index+1:index+4]):
        increases+=1
    index+=1

print(increases)
