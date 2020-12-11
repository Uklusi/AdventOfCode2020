result = 0

accum = 0

insDB = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        (instruction, value) = line.split()
        insDB.append({
            "ins": instruction,
            "val": int(value)
        })

visited = set()
index = 0

while True:
    if index in visited:
        break
    visited.add(index)
    if insDB[index]["ins"] == "nop":
        index += 1
    elif insDB[index]["ins"] == "acc":
        accum += insDB[index]["val"]
        index += 1
    elif insDB[index]["ins"] == "jmp":
        index += insDB[index]["val"]

result = accum

with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))

