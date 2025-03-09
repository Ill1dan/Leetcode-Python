def numberOfAlternatingGroups(colors, k):
    N = len(colors)
    l = 0
    res = 0

    for r in range(1, N + k - 1):
        if colors[r % N] == colors[(r - 1) % N]:
            l = r
        if r - l + 1 > k:
            l += 1
        if r - l + 1 == k:
            res += 1

    return res

colors = [0,1,0,1,0]
k = 3