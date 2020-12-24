result = 0
directions = []

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self == other
    
    def __hash__(self):
        return hash((self.x, self.y))


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
        return Coordinate(1, 0)
    elif step == "w":
        return Coordinate(-1, 0)
    elif step == "ne":
        return Coordinate(0, 1)
    elif step == "sw":
        return  Coordinate(0, -1)
    elif step == "se":
        return Coordinate(1, -1)
    elif step == "nw":
        return Coordinate(-1, 1)


tilesFlipped = set()

for tileDirection in directions:
    currentTile = Coordinate(0, 0)
    for step in tileDirection:
        currentTile += stepCoordinate(step)
    tilesFlipped ^= {currentTile}

result = len(tilesFlipped)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

