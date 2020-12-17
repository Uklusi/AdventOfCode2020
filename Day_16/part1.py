result = 0

flag = False

# Preprocessing done by hand
validMin = 26
validMax = 973

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        if line == "nearby tickets:":
            flag = True
            continue
        if flag:
            values = [int(n) for n in line.split(",")]
            for n in values:
                if n < validMin or n > validMax:
                    result += n

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))