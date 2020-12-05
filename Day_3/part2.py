result = 1

with open("input.txt", "r") as input:
    map = []
    for line in input:
        map.append(list(line.strip()))


l = len(map[0])

def checkTrees(hdis, vdis):
    tmpResult = 0
    hpos = 0
    vpos = 0

    for vpos in range(0, len(map), vdis):
        line = map[vpos]
        if line[hpos] == "#":
            tmpResult += 1
        hpos = (hpos + hdis) % l 
    return tmpResult

result *= checkTrees(1,1)
result *= checkTrees(3,1)
result *= checkTrees(5,1)
result *= checkTrees(7,1)
result *= checkTrees(1,2)

with open("output2.txt", "w") as output:
    print(str(result))
    output.write(str(result))