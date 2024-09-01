def construct2DArray(original, m, n):
    if len(original) != m * n:
        return []

    res = [[0] * n for _ in range(m)]

    for i in range(len(original)):
        res[i // n][i % n] = original[i]

    return res


original = [1, 2, 3, 4]
m = 2
n = 2
print(construct2DArray(original, m, n))