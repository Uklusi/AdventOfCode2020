result = 0

with open("input.txt", "r") as input:
    passportDatabase = []
    passport = {}
    for line in input:
        line = line.strip()
        if line == "":
            passportDatabase.append( passport )
            passport = {}
        else:
            data = line.split(" ")
            for fieldValue in data:
                (field, value) = fieldValue.split(":")
                passport[field] = value
    if passport != {}:
        passportDatabase.append( passport )

for passport in passportDatabase:
    l = len(passport.keys())
    if ( l == 8 ) or ( l == 7 and "cid" not in passport ):
        result += 1


with open("output1.txt", "w") as output:
    output.write(str(result))