result = 0

with open("input.txt", "r") as input:
    boardingDatabase = []
    for line in input:
        line = line.strip()
        textSeatId = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        seatId = int( textSeatId, 2 )
        boardingDatabase.append(seatId)
        boardingDatabase.sort()

prevSeat = boardingDatabase[0] - 1

for seat in boardingDatabase:
    if prevSeat != seat - 1:
        result = seat - 1
        break
    else: prevSeat = seat

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))