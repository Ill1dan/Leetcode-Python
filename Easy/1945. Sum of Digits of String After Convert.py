def getLucky(s, k):
    alpha_value = ""

    for i in s:
        alpha_value += str(ord(i) - 96)

    for i in range(k):
        res = 0
        for j in alpha_value:
            res += int(j)
        alpha_value = str(res)

    return res


s = "leetcode"
k = 2
print(getLucky(s, k))
