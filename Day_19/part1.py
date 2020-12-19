import functools
import re

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


explicitRule = {}


@functools.cache
def pairs(a1, b1):
    return [a + b for a in a1 for b in b1]


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
        else:
            res += pairs(
                constructRule(vs[0]),
                constructRule(vs[1])
            )
    return res


validMess = constructRule("0")

print(validMess)



with open("output1.txt", "w") as output:
    output.write(str(result))
    print(str(result))
