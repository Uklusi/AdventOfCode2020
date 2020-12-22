from collections import deque

result = 0
p1 = []
p2 = []

with open("input.txt", "r") as input:
    fileContent = input.read().strip()
    p1String, p2String = fileContent.split("\n\n")
    p1 = deque([int(n) for n in p1String.split("\n")[1:]])
    p2 = deque([int(n) for n in p2String.split("\n")[1:]])


def copyToN(queue, n):
    i = iter(queue)
    d = deque()
    for _ in range(n):
        d.append(next(i))
    return d


def recursiveCombat(p1, p2):
    states = set()
    while True:
        state = (tuple(p1), tuple(p2))
        if state in states:
            return (1, p1)
        states.add(state)
        if len(p1) == 0:
            return (2, p2)
        elif len(p2) == 0:
            return (1, p1)

        p1Val = p1.popleft()
        p2Val = p2.popleft()
        if len(p1) < p1Val or len(p2) < p2Val:
            if p1Val > p2Val:
                p1.append(p1Val)
                p1.append(p2Val)
            else:
                p2.append(p2Val)
                p2.append(p1Val)
        else:
            (subGameWinner, _) = recursiveCombat(
                copyToN(p1, p1Val),
                copyToN(p2, p2Val)
            )
            if subGameWinner == 1:
                p1.append(p1Val)
                p1.append(p2Val)
            else:
                p2.append(p2Val)
                p2.append(p1Val)


(_, winner) = recursiveCombat(p1, p2)

for i in range(1, len(winner) + 1):
    n = winner.pop()
    result += i * n

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
