result = 0

# 0 E, 1 N, 2 W, 3 S
direction = 0
dirList = ["E", "N", "W", "S"]

hval = 0
vval = 0

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        tmpAction = line[0]
        value = int(line[1:])

        if tmpAction == "F":
            action = dirList[direction]
        else:
            action = tmpAction

        if action == "E":
            hval += value
        elif action == "N":
            vval += value
        elif action == "W":
            hval -= value
        elif action == "S":
            vval -= value
        elif action == "L":
            direction = (direction + value // 90) % 4
        elif action == "R":
            direction = (direction - value // 90) % 4

result = abs(hval) + abs(vval)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

