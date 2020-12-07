result = 0

allLetters = set("qwertyuiopasdfghjklzxcvbnm")

answerDatabase = []

with open("input.txt", "r") as input:
    answerSet = allLetters.copy()
    for line in input:
        line = line.strip()
        if line == "":
            answerDatabase.append(answerSet)
            answerSet = allLetters.copy()
            newAnswers = None
        else:
            newAnswers = set(line)
            answerSet.intersection_update(newAnswers)

if newAnswers is not None:
    answerDatabase.append(answerSet)

for answer in answerDatabase:
    result += len(answer)

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

