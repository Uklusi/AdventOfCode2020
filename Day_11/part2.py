result = 0

seatDatabase = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        seatDatabase.append(list(line))

v = len(seatDatabase)
h = len(seatDatabase[0])

def checkEmpty(vpos, hpos, vdir, hdir):
    roundnum = 1
    newVpos = vpos + roundnum * vdir
    newHpos = hpos + roundnum * hdir
    while newHpos >= 0 and newHpos < h and newVpos >= 0 and newVpos < v:
        if seatDatabase[newVpos][newHpos] == "L":
            return 0
        elif seatDatabase[newVpos][newHpos] == "#":
            return 1
        else:
            roundnum += 1
            newVpos = vpos + roundnum * vdir
            newHpos = hpos + roundnum * hdir
    return 0


def changeState():
    adjOccupiedSeats = []
    nchanges = 0
    for i in range(v):
        adjOccupiedSeats.append([])
        for j in range(h):
            adjOccupiedSeats[i].append(0)

    for i in range(v):
        for j in range(h):
            adjOccupiedSeats[i][j] = sum(map(lambda a,b: checkEmpty(i,j,a,b), [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]))

    for i in range(v):
        for j in range(h):
            if seatDatabase[i][j] == "#" and adjOccupiedSeats[i][j] >= 5:
                seatDatabase[i][j] = "L"
                nchanges += 1
            elif seatDatabase[i][j] == "L" and adjOccupiedSeats[i][j] == 0:
                seatDatabase[i][j] = "#"
                nchanges += 1
    
    return nchanges

changes = -1

while changes != 0:
    changes = changeState()

result = sum( [1 for row in seatDatabase for elem in row if elem  == "#"] )

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

