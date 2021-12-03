with open("day3_input.txt", "r") as f:
    data = f.read().splitlines()

gamma, epsilon = '', ''
i = 0
while i < len(data[0]):
    zero_bits, one_bits = 0,0
    for line in data:
        if line[i] == '0':
            zero_bits += 1
        else:
            one_bits += 1
    if zero_bits > one_bits:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    i += 1

print(f"Gamma: {int(gamma, 2)}\nEpsilon: {int(epsilon, 2)}\nSolution: {int(gamma, 2)*int(epsilon, 2)}")
