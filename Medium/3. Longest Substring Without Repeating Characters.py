def lengthOfLongestSubstring(s):
    n = len(s)
    length = 0
    l = 0
    all = []

    for r in range(n):
        if s[r] not in all:
            all.append(s[r])
            length = max(length, r - l + 1)
        else:
            while s[r] in all:
                all.pop(0)
                l += 1
            all.append(s[r])

    return length


print(lengthOfLongestSubstring(""))