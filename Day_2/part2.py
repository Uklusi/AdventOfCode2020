result = 0

with open("input.txt", "r") as input:
    # passwordDatabase = []
    for line in input:
        (policy, password) = line.split(": ")
        password = password.strip()
        (num, letter) = policy.split(" ")
        (pos1, pos2) = [int(n) - 1 for n in num.split("-")]
        l = len(password)
        match1 = pos1 < l and password[pos1] == letter
        match2 = pos2 < l and password[pos2] == letter
        match = (match1 and not match2) or (match2 and not match1)
        result += int(match)

with open("output2.txt", "w") as output:
    print(str(result))
    output.write(str(result))