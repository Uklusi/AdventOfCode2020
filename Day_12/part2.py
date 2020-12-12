result = 0

wayHval = 10
wayVval = 1
hval = 0
vval = 0

def rotate(x,y, direction):
    values = [(x,y), (-y,x), (-x,-y), (y, -x)]
    return values[direction]

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        action = line[0]
        value = int(line[1:])

        if action == "E":
            wayHval += value
        elif action == "N":
            wayVval += value
        elif action == "W":
            wayHval -= value
        elif action == "S":
            wayVval -= value
        elif action == "F":
            hval += wayHval * value
            vval += wayVval * value
        elif action == "L":
            direction = (value // 90) % 4
            (wayHval, wayVval) = rotate(wayHval, wayVval, direction)
        elif action == "R":
            direction = (-value // 90) % 4
            (wayHval, wayVval) = rotate(wayHval, wayVval, direction)

result = abs(hval) + abs(vval)


with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

