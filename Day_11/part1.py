result = 0

seatDatabase = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        seatDatabase.append(list(line))

v = len(seatDatabase)
h = len(seatDatabase[0])

def changeState():
    adjOccupiedSeats = []
    nchanges = 0
    for i in range(v + 2):
        adjOccupiedSeats.append([])
        for j in range(h + 2):
            adjOccupiedSeats[i].append(0)

    for i in range(v):
        for j in range(h):
            if seatDatabase[i][j] == "#":
                adjOccupiedSeats[i-1][j-1] += 1
                adjOccupiedSeats[i-1][j  ] += 1
                adjOccupiedSeats[i-1][j+1] += 1
                adjOccupiedSeats[i  ][j-1] += 1
                adjOccupiedSeats[i  ][j+1] += 1
                adjOccupiedSeats[i+1][j-1] += 1
                adjOccupiedSeats[i+1][j  ] += 1
                adjOccupiedSeats[i+1][j+1] += 1

    for i in range(v):
        for j in range(h):
            if seatDatabase[i][j] == "#" and adjOccupiedSeats[i][j] >= 4:
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


with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

