result = 0

vals = {}

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        (command, value) = line.split(" = ")
        if command == "mask":
            mask1 = int( value.replace("0","1").replace("X","0"), base=2 )
            mask2 = int( value.replace("X","1"), base=2 )
            # print(mask1, mask2)
        else:
            value = int(value)
            index = int(command[4:-1])
            # print(value, index)
            vals[index] = (value | mask1) & mask2
            # print(vals[index])

for val in vals.values():
    result += val


with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

