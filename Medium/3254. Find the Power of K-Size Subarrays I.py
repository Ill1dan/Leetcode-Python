def resultsArray(nums, k):
    l, r = 0, k - 1
    res = []

    def issorted(arr):
        for i in range(len(arr) - 1):
            if arr[i] + 1 != arr[i + 1]:
                return -1

        return arr[-1]

    while r < len(nums):
        res.append(issorted(nums[l:r + 1]))
        l += 1
        r += 1

    return res

nums = [1, 2, 3, 4, 3, 2, 5]
k = 3
print(resultsArray(nums, k))