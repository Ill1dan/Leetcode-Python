def minimumPushes(word):
    characters = [0] * 26
    for i in word:
        characters[ord(i) - ord("a")] += 1

    characters.sort(reverse=True)

    res = 0
    multiple = 0

    for j in characters:
        res += j * (1 + multiple // 8)
        multiple += 1

    return res


word = "abcde"
print(minimumPushes(word))