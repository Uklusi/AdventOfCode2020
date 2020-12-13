result = 0

with open("input.txt", "r") as input:
    line1 = input.readline().strip()
    line2 = input.readline().strip()
    earliest = int(line1)
    busDB = [int(n) for n in line2.split(",") if n != "x"]

delayList = []

for bus in busDB:
    delay = bus - (earliest % bus)
    delayList.append(delay)

minDelay = min(delayList)

i = delayList.index(minDelay)

result = busDB[i] * minDelay

print(busDB)
print(delayList)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

