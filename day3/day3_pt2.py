
def get_key(data, op_mode):
    i = 0
    while i < len(data[0]):
        zero_bits, one_bits = 0,0
        for line in data:
            if line[i] == '0':
                zero_bits += 1
            else:
                one_bits += 1
        i += 1
    print(f"Key counts - 0: {zero_bits}; 1: {one_bits}")
    if zero_bits > one_bits and op_mode == 'o2':
        return '0'
    if zero_bits < one_bits and op_mode == 'co2':
        return '0'
    if zero_bits == one_bits and op_mode == 'co2':
        return '0'
    return '1'

def filter(data, op_mode):
    key = get_key(data, op_mode)
    new_data = []
    for line in data:
        if line.startswith(key):
            # print(key)
            # print(line)
            new_data.append(line)
            # print(new_data)
            # if len(new_data) > 5:
                # break
    if len(new_data) == 1:
        return int(new_data[0], 2)
    filter(new_data, op_mode)

def main():
    with open("day3_input.txt", "r") as f:
        data = f.read().splitlines()

    o2 = filter(data, "o2")
    co2 = filter(data, "co2")
    print(f"Final values - O2: {o2}; CO2: {co2}; Life Support: {o2*co2}")

main()
