sums = [[l for l in list(s) if l != " "] for s in open("Day18.txt")]

def apply(operands, operators):
    o1 = operands.pop()
    o2 = operands.pop()
    return (o1 + o2 if operators.pop() == "+" else o1 * o2)

def doSums(s, precedence, operands=[], operators = []):
    for token in s:
        if token in ("+", "*"):
            while len(operators) and operators[-1] != "(" and precedence(token) <= precedence(operators[-1]):
                operands.append(apply(operands, operators))
            operators.append(token)
        elif token.isdigit():
            operands.append(int(token))
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while len(operators) and operators[-1] != "(":
                operands.append(apply(operands, operators))
            operators.pop()
    while len(operators):
        operands.append(apply(operands, operators))
    return operands[-1]

print sum(doSums(s, lambda op: 1) for s in sums)
print sum(doSums(s, lambda op: 2 if op == "+" else 1) for s in sums)
