result = 1

initialSubjectNumber = 7
cardPublicKey = 0
doorPublicKey = 0
modulo = 20201227

with open("input.txt", "r") as input:
    (cardPublicKey, doorPublicKey) = map(int, input.read().strip().split("\n"))

cardLoopSize = 0
calculatedPublicKey = 1
while calculatedPublicKey != cardPublicKey:
    calculatedPublicKey = (calculatedPublicKey * initialSubjectNumber) % modulo
    cardLoopSize += 1

# doorLoopSize = 0
# calculatedPublicKey = 1
# while calculatedPublicKey != doorPublicKey:
#     calculatedPublicKey = (calculatedPublicKey * initialSubjectNumber) % modulo
#     doorLoopSize += 1

for i in range(cardLoopSize):
    result = (result * doorPublicKey) % modulo

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

