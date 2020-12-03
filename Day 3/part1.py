result = 0

with open("input.txt", "r") as input:
    map = []
    for line in input:
        map.append(list(line.strip()))

hpos = 0

l = len(map[1])

for line in map:
    if line[hpos] == "#":
        result += 1
    hpos = (hpos + 3) % l 


with open("output1.txt", "w") as output:
    output.write(str(result))