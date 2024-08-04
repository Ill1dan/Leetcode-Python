def rangeSum(nums, n, left, right):
    subarray = []
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            subarray.append(s)

    subarray.sort()
    mod = 1e9 + 7

    return int(sum(subarray[left - 1: right]) % mod)

nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
print(rangeSum(nums, n, left, right))