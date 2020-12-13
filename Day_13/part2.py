result = 0

# Copiata beceramente, inverso di A mod n
modInverse = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or modInverse(n, A%n, t, s-A//n*t, N or n),-1)[n<1]

with open("input.txt", "r") as input:
    line1 = input.readline().strip()
    line2 = input.readline().strip()
    line2Arr = line2.split(",")
    busDB = [int(n) for n in line2Arr if n != "x"]
    delayDB = [line2Arr.index(str(n)) for n in busDB]

l = len(busDB)

delayDB = [-delayDB[i] % busDB[i] for i in range(l) ]

p = 1
for n in busDB:
    p *= n
otherProd = []
for n in busDB: 
    otherProd.append(p // n)

modInvs = [modInverse(otherProd[i], busDB[i]) * delayDB[i] % busDB[i] for i in range(l)]

for i in range(l):
    result += modInvs[i] * otherProd[i]

result = result % p

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

