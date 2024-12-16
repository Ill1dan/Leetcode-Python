def getFinalState(nums, k, multiplier):
    for _ in range(k):
        # Find the index of the minimum value. If there are multiple, pick the first one.
        min_index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[min_index]:
                min_index = i

        # Update the minimum value by multiplying it with the multiplier
        nums[min_index] *= multiplier

    return nums

nums = [2,1,3,5,6]
k = 5
multiplier = 2
print(getFinalState(nums, k, multiplier))