def twoSum(nums, target):
    dict = {}
    for x in nums:
        new = target - x
        if x not in dict:
            dict[new] = 0
        else:
            dict[x] += 1

    for i, j in dict.items():
        if j == 1:
            num = [i, target - i]

    index = []
    count = 0
    for z in nums:
        if z in num:
            index.append(count)
        count += 1

    return index

twoSum([2,7,11,15], 9)
