from math import lcm, gcd

def fractionAddition(expression):
    numerators = []
    denominators = []
    signs = [] if expression[0] == "-" else ["+"]
    flag = False if expression[0] == "-" else True
    num = ""

    for i in expression:
        if i == "+" or i == "-" or i == "/":
            if num and flag:
                numerators.append(int(num))
            elif num and not flag:
                denominators.append(int(num))
            flag = not flag
            num = ""

            if i != "/":
                signs.append(i)
        else:
            num += i

    denominators.append(int(num))

    denominator = 1
    numerator = 0

    for i in denominators:
        denominator = lcm(i, denominator)

    for i in range(len(numerators)):
        if signs[i] == "+":
            numerator += (numerators[i] * (denominator // denominators[i]))
        else:
            numerator -= (numerators[i] * (denominator // denominators[i]))

    common_divisor = gcd(abs(numerator), denominator)

    numerator //= common_divisor
    denominator //= common_divisor

    return f"{numerator}/{denominator}"


expression = "-5/2+10/3+7/9"
print(fractionAddition(expression))
