result = 0

answerDatabase = []

with open("input.txt", "r") as input:
    answerSet = set()
    for line in input:
        line = line.strip()
        if line == "":
            answerDatabase.append(answerSet)
            answerSet = set()
        else:
            for letter in line:
                answerSet.add(letter)

if len(answerSet) != 0:
    answerDatabase.append(answerSet)
    answerSet = set()

for answer in answerDatabase:
    result += len(answer)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

