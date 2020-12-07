import re

result = 0

inToOutDatabase = {}
outToInDatabase = {}

listSepRegex = re.compile( r" bags?(?:, |\.)" )
numRegex = re.compile( r"([0-9]+) " )

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        (outerBag, innerListString) = line.split(" bags contain ")
        
        outToInDatabase[outerBag] = []
        if not innerListString == "no other bags.":
            innerList = listSepRegex.split(innerListString)
            innerList.pop()
            for inner in innerList:
                # print(inner)
                (_, innerQuantity, innerBag) = numRegex.split(inner)
                innerQuantity = int(innerQuantity)
                outToInDatabase[outerBag].append({"bag": innerBag, "quantity": innerQuantity})
                if innerBag not in inToOutDatabase:
                    inToOutDatabase[innerBag] = []
                inToOutDatabase[innerBag].append(outerBag)

bagsContained = {}

def checkInner(bag):
    if bag in bagsContained:
        return bagsContained[bag]
    numBags = 1
    for data in outToInDatabase[bag]:
        innerBag = data["bag"]
        innerQuantity = data["quantity"]
        numBags += (checkInner(innerBag) * innerQuantity)
    bagsContained[bag] = numBags
    return numBags


result = checkInner("shiny gold") -1


with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
