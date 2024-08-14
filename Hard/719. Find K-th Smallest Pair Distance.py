def smallestDistancePair(nums, k):
    nums.sort()

    def pair(diff):
        i = 0
        res = 0

        for j in range(len(nums)):
            while nums[j] - nums[i] > diff:
                i += 1
            res += j - i

        return res

    l, r = 0, max(nums)
    while l < r:
        m = l + ((r - l) // 2)
        total_pairs = pair(m)
        if total_pairs >= k:
            r = m
        else:
            l = m + 1

    return r


nums = [62, 100, 4]
k = 2
print(smallestDistancePair(nums, k))
