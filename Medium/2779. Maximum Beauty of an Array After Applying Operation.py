def maximumBeauty(nums, k):
    nums.sort()
    res = 0
    l = 0

    for r in range(len(nums)):
        while nums[r] - nums[l] > 2 * k:
            l += 1
        res = max(res, r - l + 1)

    return res


nums = [4,6,1,2]
k = 2
print(maximumBeauty(nums, k))