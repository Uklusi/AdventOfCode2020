result = 0

active = []

y = 0
z = 0
w = 0
with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        l = len(line)
        for x in range(l):
            if line[x] == "#":
                active.append((x, y, z, w))
        y -= 1

toll = (-1, 0, 1)


def neighbours(pos):
    return [
        (pos[0] + a, pos[1] + b, pos[2] + c, pos[3] + d)
        for a in toll for b in toll for c in toll for d in toll
        if (a, b, c, d) != (0, 0, 0, 0)
    ]


def isAlive(pos):
    return pos in activeNeighs and (
        activeNeighs[pos] == 3 or (
            pos in active and activeNeighs[pos] == 2
        )
    )


for c in range(6):
    newActive = []
    activeNeighs = {}
    for pos in active:
        for ne in neighbours(pos):
            if ne not in activeNeighs:
                activeNeighs[ne] = 1
            else:
                activeNeighs[ne] += 1
    for pos in activeNeighs:
        if isAlive(pos):
            newActive.append(pos)
    active = newActive

result = len(active)

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
