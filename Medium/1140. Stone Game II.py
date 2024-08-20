def stoneGameII(piles):
    dp = {}

    def recursive(alice, i, M):
        if i == len(piles):
            return 0

        if (alice, i, M) in dp:
            return dp[(alice, i, M)]

        res = 0 if alice else float("inf")
        total = 0

        for x in range(1, 2 * M + 1):
            if i + x > len(piles):
                break
            total += piles[i + x - 1]

            if alice:
                res = max(res, total + recursive(not alice, i + x, max(M, x)))
            else:
                res = min(res, recursive(not alice, i + x, max(M, x)))

        dp[(alice, i, M)] = res
        return res

    return recursive(True, 0, 1)


piles = [2, 7, 9, 4, 4]
print(stoneGameII(piles))