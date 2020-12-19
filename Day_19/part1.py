import functools

rules = {}
messages = set()
flag = False

with open("input.txt", "r") as input:
    for line in input:
        line = line.strip()
        if line == "":
            flag = True
        elif not flag:
            (num, rule) = line.split(": ")
            rules[num] = rule
        else:
            messages.add(line)


@functools.cache
def constructRule(ruleName):
    rule = rules[ruleName]
    if "|" in rule:
        rs = rule.split(" | ")
    else:
        rs = [rule]
    res = []
    for r in rs:
        vs = r.split(" ")
        if '"' in vs[0]:
            res = [vs[0].strip('"')]
        elif len(vs) == 1:
            res += constructRule(vs[0])
        elif ruleName not in vs:
            res += [
                a + b
                for a in constructRule(vs[0])
                for b in constructRule(vs[1])
            ]
    return res


validMess = set(constructRule("0"))

result = len(validMess.intersection(messages))


with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
