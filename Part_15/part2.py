result = 0

revDict = {}
seq = []
count = 0

with open("input.txt", "r") as input:
    line = input.readline().strip()
    seq = [int(n) for n in line.split(",")]

for n in seq:
    count += 1
    revDict[n] = [count]
    prevNum = n
    # print(prevNum)

def insertLastNum(n, count, prevPos):
    if n not in prevPos:
        prevPos[n] = [count]
    else:
        prevPos[n] = [count, prevPos[n][0]]

while count < 30000000:
    count += 1
    n = prevNum
    if len(revDict[n]) == 1:
        prevNum = 0
    else:
        prevNum = revDict[n][0] - revDict[n][1]
    # print(prevNum)
    insertLastNum(prevNum, count, revDict)

result = prevNum

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))