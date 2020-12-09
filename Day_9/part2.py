result = 0

numberList = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        numberList.append(int(line))

l = len(numberList)

for i in range(l):
    if i < 25:
        pass
    else:
        prevlist = set()
        for j in range(i-25, i):
            prevlist.update({numberList[j] + numberList[k] for k in range(j+1, i)})
        if numberList[i] not in prevlist:
            wrongNum = numberList[i]
            break

for i in range(l):
    s = 0
    j = 1
    while s < wrongNum and i+j < l:
        s = sum(numberList[i:i+j+1])
        j += 1
    if s != wrongNum:
        continue
    else:
        result = min(numberList[i:i+j]) + max(numberList[i:i+j])

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

