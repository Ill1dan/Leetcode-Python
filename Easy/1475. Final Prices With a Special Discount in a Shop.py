def finalPrices(prices):
    n = len(prices)
    result = prices[:]  # Copy of prices to store final results

    for i in range(n):
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                result[i] = prices[i] - prices[j]
                break  # Stop at the first valid discount

    return result

prices = [8,4,6,2,3]
print(finalPrices(prices))