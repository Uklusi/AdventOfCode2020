result = 0


with open("input.txt", "r") as input:
    fileContent = input.read().strip()
    cups = [int(n) for n in fileContent]


def rotate(cups, n):
    return cups[n:] + cups[:n]


def insertAt(cups, n, ins):
    return cups[:n] + ins + cups[n:]


for _ in range(100):
    currCup = cups[0]
    crab = cups[1:4]
    del(cups[1:4])
    pos = currCup - 1
    while pos not in cups:
        pos = pos - 1
        if pos <= 0:
            pos = max(cups)
    cups = insertAt(cups, cups.index(pos) + 1, crab)
    crab = []
    cups = rotate(cups, 1)

cups = rotate(cups, (cups.index(1) + 1) % len(cups))
cups.pop()

result = "".join([str(c) for c in cups])

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
