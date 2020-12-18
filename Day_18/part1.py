import re


def solveString(string):
    string = string.strip("()")
    stringArr = string.split()
    while len(stringArr) > 1:
        if stringArr[1] == "+":
            r = int(stringArr[0]) + int(stringArr[2])
        elif stringArr[1] == "*":
            r = int(stringArr[0]) * int(stringArr[2])
        else:
            print("ERROR")
        stringArr.pop(1)
        stringArr.pop(1)
        stringArr[0] = str(r)
    return str(r)


def solveMatch(match):
    return solveString(match.group(0))

result = 0

parensRe = re.compile(r'\([^()]+\)')

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        while line.count("(") > 0:
            line = parensRe.sub(solveMatch, line)
        result += int(solveString(line))


with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
