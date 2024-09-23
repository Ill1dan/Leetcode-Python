from collections import Counter

def minExtraChar(s, dictionary):
    n = len(s)

    def dp(i: int, extra: int) -> int:
        if i >= n:
            return extra

        min_extra = dp(i + 1, extra)
        for word in dictionary:
            if s[i:].startswith(word):
                min_extra = min(min_extra, dp(i + len(word), extra - len(word)))

        return min_extra

    return dp(0, n)


s = "dwmodizxvvbosxxw"
dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
print(minExtraChar(s, dictionary))