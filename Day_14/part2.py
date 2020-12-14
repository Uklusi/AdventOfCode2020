result = 0

vals = {}

def maskValues(strMask, values):
    if strMask.count('X') == 0:
        return values
    i = strMask.find('X')
    newValues = [s[:i] + '0' + s[i+1:] for s in values] + [s[:i] + '1' + s[i+1:] for s in values]
    newStrMask = strMask[:i] + '0' + strMask[i+1:]
    return maskValues(newStrMask, newValues)



with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        (command, value) = line.split(" = ")
        if command == "mask":
            mask = value
            mask1 = int( value.replace("X","0"), base=2 )
            # print(mask1, mask2)
        else:
            value = int(value)
            index = int(command[4:-1])
            # print(value, index)
            index = index | mask1
            strIndex = format(index,'036b')
            # print(strIndex)
            # print(mask)
            indexList = maskValues(mask, [strIndex])

            for strI in indexList:
                i = int(strI, 2)
                vals[i] = value

            # print(vals[index])

for val in vals.values():
    result += val
# print(vals)

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

