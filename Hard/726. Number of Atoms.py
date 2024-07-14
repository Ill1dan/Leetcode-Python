from collections import Counter

def countOfAtoms(formula):
    stack = [Counter()]
    i = 0
    x = len(formula)

    while i < x:
        if formula[i] == '(':
            stack.append(Counter())
            i += 1
        elif formula[i] == ')':
            i += 1
            start = i
            while i < x and formula[i].isdigit():
                i += 1
            number = int(formula[start:i] or 1)
            top = stack.pop()
            for element, total in top.items():
                stack[-1][element] += total * number
        else:
            start = i
            i += 1
            while i < x and formula[i].islower():
                i += 1
            element = formula[start:i]
            start = i
            while i < x and formula[i].isdigit():
                i += 1
            total = int(formula[start:i] or 1)
            stack[-1][element] += total

    final = stack.pop()
    sorted_final = sorted(final.items())
    output = []
    
    for element, total in sorted_final:
        output.append(element)
        if total > 1:
            output.append(str(total))

    return "".join(output)

formula = "K4(ON(SO3)2)2"
print(countOfAtoms(formula))

