result = 0

with open("input.txt", "r") as input:
    boardingDatabase = []
    for line in input:
        line = line.strip()
        textSeatId = line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
        seatId = int( textSeatId, 2 )

        if seatId > result:
            result = seatId



with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))