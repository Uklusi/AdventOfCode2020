import functools
import re

result = 0
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


validMess42 = constructRule("42")
validMess31 = constructRule("31")

regexp42 = "|".join(validMess42)
regexp31 = "|".join(validMess31)
regexp = re.compile("({0})({0})+({1})+".format(regexp42, regexp31))
regexpsub = re.compile("^(?:{0})((?:{0})*(?:{1})*)(?:{1})$".format(regexp42, regexp31))
regexpcheck = re.compile("^(?:{0})+$".format(regexp42))


m1 = [m for m in messages if regexp.fullmatch(m)]
for m in m1:
    while regexpsub.match(m):
        m = regexpsub.sub(r"\1", m)
    if regexpcheck.match(m):
        result += 1


with open("output2.txt", "w") as output:
    output.write(str(result))
    print(str(result))
