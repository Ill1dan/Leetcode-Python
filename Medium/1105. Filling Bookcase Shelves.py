def minHeightShelves(books, shelfWidth):
    n = len(books)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        cur_width = shelfWidth
        max_width = 0
        dp[i] = float("inf")
        for j in range(i, n):
            width, height = books[j]
            if cur_width < width:
                break
            cur_width -= width
            max_width = max(max_width, height)
            dp[i] = min(dp[i], dp[j + 1] + max_width)
    return dp[0]

books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
shelfWidth = 4
print(minHeightShelves(books, shelfWidth))