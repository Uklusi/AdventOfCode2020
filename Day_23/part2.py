result = 0
MAXCUP = 1000000
MAXITER = 10000000
MAXCUPININPUT = 9
INPUTL = MAXCUPININPUT + 1


with open("input.txt", "r") as input:
    fileContent = input.read().strip()
    cups = [int(n) for n in fileContent]

nextVals = [0] + [
    INPUTL if i == cups[-1] else cups[cups.index(i) + 1]
    for i in range(1, INPUTL)
]

nextVals.extend(range(INPUTL + 1, MAXCUP + 1))
nextVals.append(cups[0])

currNode = cups[0]
for i in range(MAXITER):
    a = nextVals[currNode]
    b = nextVals[a]
    c = nextVals[b]
    nextVals[currNode] = nextVals[c]
    n = currNode - 1
    while n in (0, a, b, c):
        if n == 0:
            n = MAXCUP
        else:
            n -= 1
    x = nextVals[n]
    nextVals[n] = a
    nextVals[c] = x
    currNode = nextVals[currNode]

a = nextVals[1]
b = nextVals[a]

result = a * b

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
