def canBeEqual(target, arr):
    dict1 = {}
    dict2 = {}

    for x in target:
        if x not in dict1:
            dict1[x] = 1
        else:
            dict1[x] += 1

    for y in arr:
        if y not in dict2:
            dict2[y] = 1
        else:
            dict2[y] += 1

    if len(dict1) != len(dict2):
        return False

    for i in dict1:
        if i not in dict2:
            return False

        if dict1[i] != dict2[i]:
            return False

    return True


target = [1, 2, 3, 4]
arr = [2, 4, 1, 3]
print(canBeEqual(target, arr))