result = 0

flag = "F"  # Fields

# Preprocessing done by hand
validMin = 26
validMax = 973

namesDB = []
fieldsDB = []

tickets = []

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()

        if line == "":
            continue
        elif line == "nearby tickets:" or line == "your ticket:":
            flag = "T"  # Tickets
            continue
        elif flag == "F":
            field, values = line.split(": ")
            values = [int(n) for v in values.split(" or ") for n in v.split("-")]
            namesDB.append(field)
            fieldsDB.append(values)

        elif flag == "T":
            ticketFlag = True
            values = [int(n) for n in line.split(",")]
            for n in values:
                if n < validMin or n > validMax:
                    ticketFlag = False
            if ticketFlag:
                tickets.append(values)

l = len(namesDB)

# validation[i][j] is "Ticket place i can be field j"
validation = []
for i in range(l):
    validation.append([True, ]*l)

for i in range(l):
    for j in range(l):
        for ticket in tickets:
            v = ticket[i]
            validation[i][j] = validation[i][j] and (
                (
                    v >= fieldsDB[j][0] and v <= fieldsDB[j][1]
                ) or (
                    v >= fieldsDB[j][2] and v <= fieldsDB[j][3]
                )
            )


def prod(vals):
    p = 1
    for i in vals:
        p *= i
    return p


print("\n".join([",".join(["1" if i else "0" for i in v]) for v in validation]))
print("")

alreadyCorrected = []

while prod([sum(v) for v in validation]) > 1:
    for i in range(l):
        if validation[i].count(True) == 1 and i not in alreadyCorrected:
            alreadyCorrected.append(i)
            j = validation[i].index(True)
            for k in range(l):
                if k == i:
                    continue
                else:
                    validation[k][j] = False

vals = [i for i in range(l) for j in range(6) if validation[i][j]]

# print(vals)
t = tickets[0]
result = prod([t[v] for v in vals])

with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
