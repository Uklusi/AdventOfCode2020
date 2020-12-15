result = 0

revDict = {}

with open("input.txt", "r") as input:
    line = input.readline().strip()
    seq = [int(n) for n in line.split(",")]

count = 0
for n in seq:
    count += 1
    revDict[n] = count
    prevNum = n

prevNum = 0

while count < 30000000 -1:
    count += 1

    if prevNum not in revDict:
        n = 0
    else:
        n = count - revDict[prevNum]
    
    revDict[prevNum] = count
    prevNum = n
        
result = prevNum

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))