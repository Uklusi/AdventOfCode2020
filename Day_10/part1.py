result = 0

adapterList = [0]

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        adapterList.append(int(line))

adapterList.sort()

n = [0,0,0,1]

for i in range(1,len(adapterList)):
    diff = adapterList[i] - adapterList[i-1]
    n[diff] += 1

result = n[1]*n[3]

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

