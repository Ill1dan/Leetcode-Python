def countConsistentStrings(allowed, words):
    allowed = set(allowed)
    res = 0

    for i in words:
        word = set(i)

        for j in word:
            if j not in allowed:
                res -= 1
                break
        res += 1

    return res


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
print(countConsistentStrings(allowed, words))