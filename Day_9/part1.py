result = 0

numberList = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        numberList.append(int(line))

for i in range(len(numberList)):
    if i < 25:
        pass
    else:
        prevlist = set()
        for j in range(i-25, i):
            prevlist.update({numberList[j] + numberList[k] for k in range(j+1, i)})
        if numberList[i] not in prevlist:
            result = numberList[i]
            break


with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

