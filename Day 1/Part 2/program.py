with open("input.txt", "r") as input:
    numList = [ int(num) for num in input]

result = 0

l = len(numList)

for ii in range(l):
    i = numList[ii]
    for ij in range(ii+1, l):
        j = numList[ij]
        for ik in range(ij+1, l):
            k = numList[ik]
            if i+j+k == 2020:
                result = i*j*k

with open("output.txt", "w") as output:
    output.write(str(result))