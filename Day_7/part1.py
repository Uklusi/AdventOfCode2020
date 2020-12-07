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
        if innerListString == "no other bags.":
            outToInDatabase[outerBag] = None
        else:
            innerList = listSepRegex.split(innerListString)
            innerList.pop()
            outToInDatabase[outerBag] = []
            for inner in innerList:
                # print(inner)
                (_, innerQuantity, innerBag) = numRegex.split(inner)
                innerQuantity = int(innerQuantity)
                outToInDatabase[outerBag].append({"bag": innerBag, "quantity": innerQuantity})
                if innerBag not in inToOutDatabase:
                    inToOutDatabase[innerBag] = []
                inToOutDatabase[innerBag].append(outerBag)

checkedOuterBags = []

def checkOuter(bag):
    if bag in checkedOuterBags:
        return
    checkedOuterBags.append(bag)
    if bag not in inToOutDatabase:
        return
    for outerBag in inToOutDatabase[bag]:
        checkOuter(outerBag)

checkOuter("shiny gold")
checkedOuterBags.remove("shiny gold")

# print(inToOutDatabase)
result = len(checkedOuterBags)

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

