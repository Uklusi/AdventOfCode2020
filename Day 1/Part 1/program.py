with open("input.txt", "r") as input:
    numList = [ int(num) for num in input]

result = 0

for i in numList:
    for j in numList:
        if i+j == 2020:
            result = i*j

with open("output.txt", "w") as output:
    output.write(str(result))