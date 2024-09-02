def chalkReplacer(chalk, k):
    n = sum(chalk)
    k %= n

    for i in range(len(chalk)):
        if chalk[i] > k:
            return i

        k -= chalk[i]


chalk = [3, 4, 1, 2]
k = 25
print(chalkReplacer(chalk, k))