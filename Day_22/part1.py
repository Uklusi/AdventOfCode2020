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

while len(p1) > 0 and len(p2) > 0:
    p1Val = popLeft(p1)
    p2Val = popLeft(p2)
    if p1Val > p2Val:
        p1.append(p1Val)
        p1.append(p2Val)
    else:
        p2.append(p2Val)
        p2.append(p1Val)

winner = (p1 if len(p1) > 0 else p2).copy()

for i in range(1, len(winner) + 1):
    n = winner.pop()
    result += i * n

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
