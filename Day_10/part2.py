result = 1

adapterList = [0]

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        adapterList.append(int(line))

adapterList.sort()
adapterList.append(adapterList[-1]+3)

diffs = [[]]

prevdiff = -1
currind = 0

for i in range(1,len(adapterList)):
    diff = adapterList[i] - adapterList[i-1]
    if diff == 3:
        currind += 1
        diffs.append([3])
    elif diff == 2:
        if prevdiff in [2,3]:
            currind += 1
            diffs.append([2])
        else:
            diffs[currind].append(2)
    elif diff == 1:
        diffs[currind].append(1)
    prevdiff = diff

def calcNumPoss(ldiff):
    if len(ldiff) in [0,1]:
        return 1
    x = ldiff[0] + ldiff[1]
    if x <= 3:
        return calcNumPoss(ldiff[1:]) + calcNumPoss([x] + ldiff[2:])
    else:
        return calcNumPoss(ldiff[1:])
        
for ldiff in diffs:
    result *= calcNumPoss(ldiff)



with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

