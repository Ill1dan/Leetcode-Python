def maximumGain(s, x, y):
    if y > x:
        first = "b"
        second = "a"
        main = y
        sec_main = x
    else:
        first = "a"
        second = "b"
        main = x
        sec_main = y

    stack = []
    score = 0

    for i in s:
        if i != second:
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
            elif stack[-1] == first:
                stack.pop(-1)
                score += main
            else:
                stack.append(i)

    stack2 = []

    for j in stack:
        if j != first:
            stack2.append(j)
        else:
            if len(stack2) == 0:
                stack2.append(j)
            elif stack2[-1] == second:
                stack2.pop(-1)
                score += sec_main
            else:
                stack2.append(j)

    return score

s = "aabbaaxybbaabb"
x = 5
y = 4

print(maximumGain(s, x, y))