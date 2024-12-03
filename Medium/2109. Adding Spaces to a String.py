def addSpaces(s, spaces):
    i, j = 0, 0
    res = []

    while i < len(s) and j < len(spaces):
        if i < spaces[j]:
            res.append(s[i])
            i += 1
        else:
            res.append(" ")
            j += 1

    if i < len(s):
        res.append(s[i:])

    return "".join(res)


s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]
print(addSpaces(s, spaces))