from copy import deepcopy
result = 0

insDB = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        (instruction, value) = line.split()
        insDB.append({
            "ins": instruction,
            "val": int(value)
        })

origDB = deepcopy(insDB)

def traverse():
    visited = set()
    index = 0
    accum = 0
    while True:
        if index in visited:
            return None
        if index >= len(insDB):
            return accum
        visited.add(index)
        if insDB[index]["ins"] == "nop":
            index += 1
        elif insDB[index]["ins"] == "acc":
            accum += insDB[index]["val"]
            index += 1
        elif insDB[index]["ins"] == "jmp":
            index += insDB[index]["val"]

for index in range(len(origDB)):
    if origDB[index]["ins"] == "nop":
        insDB[index]["ins"] = "jmp"
    elif origDB[index]["ins"] == "jmp":
        insDB[index]["ins"] = "nop"
    else:
        continue
    ret = traverse()
    if ret is None:
        if origDB[index]["ins"] == "nop":
            insDB[index]["ins"] = "nop"
        elif origDB[index]["ins"] == "jmp":
            insDB[index]["ins"] = "jmp"
    else:
        result = ret
        break


with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))

