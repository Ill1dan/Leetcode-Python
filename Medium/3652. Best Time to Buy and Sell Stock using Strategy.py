class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)

        actualP = 0
        profit = [0] * n

        for i in range(n):
            profit[i] = strategy[i] * prices[i]
            actualP += profit[i]

        originalWindProfit = 0
        modifiedWindProfit = 0
        maxGain = 0

        i = 0
        j = 0

        # sliding window
        while j < n:
            originalWindProfit += profit[j]

            # second half of the window contributes to modifiedWindProfit
            if j - i + 1 > k // 2:
                modifiedWindProfit += prices[j]

            if j - i + 1 > k:
                originalWindProfit -= profit[i]
                modifiedWindProfit -= prices[i + k // 2]
                i += 1

            # evaluate window of size k
            if j - i + 1 == k:
                maxGain = max(maxGain, modifiedWindProfit - originalWindProfit)

            j += 1

        return actualP + maxGain
        