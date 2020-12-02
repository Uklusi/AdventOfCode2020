result = 0

with open("input.txt", "r") as input:
    # passwordDatabase = []
    for line in input:
        (policy, password) = line.split(": ")
        password = password.strip()
        (num, letter) = policy.split(" ")
        (minNum, maxNum) = [int(n) for n in num.split("-")]
        count = password.count(letter)
        result += int( count >= minNum and count <= maxNum )
        # passwordDatabase.append(
        #     {
        #         "letter": letter,
        #         "minNum": minNum,
        #         "maxNum": maxNum,
        #         "password": password
        #     }
        # )



with open("output.txt", "w") as output:
    output.write(str(result))