def minSwaps(nums):
    n = len(nums)
    ones = sum(nums)
    i = 0
    window_ones = max_window_ones = 0
    for x in range(2 * n):
        if nums[x % n]:
            window_ones += 1
        if x - i + 1 > ones:
            window_ones -= nums[i % n]
            i += 1
        max_window_ones = max(max_window_ones, window_ones)

    return ones - max_window_ones


nums = [0, 1, 0, 1, 1, 0, 0]
print(minSwaps(nums))