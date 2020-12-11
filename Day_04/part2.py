import re

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

fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

yearPattern = re.compile( r"^\d{4}$" )
hgtPattern = re.compile( r"^\d{3}cm|\d{2}in$" )
hairPattern = re.compile( r"^#[\da-f]{6}$" )
eyeSet = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
pidPattern = re.compile( r"^\d{9}$" )


for passport in passportDatabase:
    # print("fields")
    if not fields.issubset(passport.keys()):
        continue
    # print("byr")
    strVal = passport["byr"]
    if yearPattern.match( strVal ) is None:
        continue
    val = int( strVal )
    if val < 1920 or val > 2002:
        continue
    # print("iyr")
    strVal = passport["iyr"]
    if yearPattern.match( strVal ) is None:
        continue
    val = int( strVal )
    if val < 2010 or val > 2020:
        continue
    # print("eyr")
    strVal = passport["eyr"]
    if yearPattern.match( strVal ) is None:
        continue
    val = int( strVal )
    if val < 2020 or val > 2030:
        continue
    strVal = passport["hgt"]
    if hgtPattern.match( strVal ) is None:
        continue
    (val, unit) = ( int(strVal[:-2]), strVal[-2:] )
    if unit == "cm":
        if val < 150 or val > 193:
            continue
    elif unit == "in":
        if val < 59 or val > 76:
            continue
    strVal = passport["hcl"]
    if hairPattern.match( strVal ) is None:
        continue
    strVal = passport["ecl"]
    if not strVal in eyeSet:
        continue
    strVal = passport["pid"]
    if pidPattern.match( strVal ) is None:
        continue
    result += 1

with open("output2.txt", "w") as output:
    print(str(result))
    output.write(str(result))