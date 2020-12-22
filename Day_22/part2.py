result = 0
p1 = []
p2 = []


def popLeft(queue):
    val = queue[0]
    queue.remove(queue[0])
    return val


with open("input.txt", "r") as input:
    fileContent = input.read().strip()
    p1String, p2String = fileContent.split("\n\n")
    p1 = [int(n) for n in p1String.split("\n")[1:]]
    p2 = [int(n) for n in p2String.split("\n")[1:]]


def recursiveCombatRound(p1, p2):
    p1Val = popLeft(p1)
    p2Val = popLeft(p2)
    if len(p1) < p1Val or len(p2) < p2Val:
        if p1Val > p2Val:
            p1.append(p1Val)
            p1.append(p2Val)
        else:
            p2.append(p2Val)
            p2.append(p1Val)
    else:
        subGameWinner = recursiveCombat(p1[:p1Val], p2[:p2Val])[0]
        if subGameWinner == 1:
            p1.append(p1Val)
            p1.append(p2Val)
        else:
            p2.append(p2Val)
            p2.append(p1Val)
    return (p1, p2)


def recursiveCombat(p1, p2):
    states = set()
    while True:
        state = ",".join([str(n) for n in p1]) + "|" + ",".join([str(n) for n in p2])
        if state in states:
            return (1, p1, p2)
        states.add(state)
        if len(p1) == 0:
            return (2, p1, p2)
        elif len(p2) == 0:
            return (1, p1, p2)
        (p1, p2) = recursiveCombatRound(p1, p2)


res = recursiveCombat(p1, p2)

winner = res[res[0]]

for i in range(1, len(winner) + 1):
    n = winner.pop()
    result += i * n

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
