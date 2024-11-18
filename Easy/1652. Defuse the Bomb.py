def decrypt(code, k):
    n = len(code)
    res = []

    if k > 0:
        for i in range(n):
            total = 0
            for j in range(1, k + 1):
                total += code[(i + j) % n]
            res.append(total)
    elif k < 0:
        k = abs(k)
        for i in range(n):
            total = 0
            for j in range(1, k + 1):
                total += code[(i - j) % n]
            res.append(total)
    else:
        res = [0] * n

    return res

code = [2,4,9,3]
k = -2
print(decrypt(code, k))