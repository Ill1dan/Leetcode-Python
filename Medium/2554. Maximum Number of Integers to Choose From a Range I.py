def maxCount(banned, n, maxSum):
    banned = set(banned)
    total = 0
    res = 0

    for i in range(1, n + 1):
        if i not in banned and total + i <= maxSum:
            total += i
            res += 1

    return res


banned = [1,6,5]
n = 5
maxSum = 6
print(maxCount(banned, n, maxSum))