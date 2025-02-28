def shortestCommonSupersequence(str1, str2):
    # DP Solution
    N, M = len(str1), len(str2)

    prev = [str2[j:] for j in range(M)]
    prev.append("")

    for i in reversed(range(N)):
        cur = [""] * M
        cur.append(str1[i:])
        for j in reversed(range(M)):
            if str1[i] == str2[j]:
                cur[j] = str1[i] + prev[j + 1]
            else:
                res1 = str1[i] + prev[j]
                res2 = str2[j] + cur[j + 1]
                if len(res1) < len(res2):
                    cur[j] = res1
                else:
                    cur[j] = res2
        prev = cur

    return cur[0]

    # Backtracking Solution
    cache = {}

    def backtrack(i, j):
        if (i, j) in cache:
            return cache[(i, j)]
        if i == len(str1):
            return str2[j:]
        if j == len(str2):
            return str1[i:]

        if str1[i] == str2[j]:
            return str1[i] + backtrack(i + 1, j + 1)

        res1 = str1[i] + backtrack(i + 1, j)
        res2 = str2[j] + backtrack(i, j + 1)
        if len(res1) < len(res2):
            cache[(i, j)] = res1
            return res1
        cache[(i, j)] = res2
        return res2

    return backtrack(0, 0)

str1 = "abac"
str2 = "cab"
print(shortestCommonSupersequence(str1, str2))