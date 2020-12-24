result = 0
directions = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        currentDirection = []
        step = ""
        for c in line:
            step = step + c
            if c in ("e", "w"):
                currentDirection.append(step)
                step = ""
        directions.append(currentDirection)


def stepCoordinate(step):
    if step == "e":
        return (1, 0)
    elif step == "w":
        return (-1, 0)
    elif step == "ne":
        return (0, 1)
    elif step == "sw":
        return  (0, -1)
    elif step == "se":
        return (1, -1)
    elif step == "nw":
        return (-1, 1)

def addCoords(a, b):
    return (a[0] + b[0], a[1] + b[1])


tilesFlipped = set()

for tileDirection in directions:
    currentTile = (0, 0)
    for step in tileDirection:
        currentTile = addCoords(currentTile, stepCoordinate(step))
    # print(currentTile)
    tilesFlipped ^= {currentTile}

result = len(tilesFlipped)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

