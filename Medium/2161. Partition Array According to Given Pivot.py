def pivotArray(nums, pivot):
    less = []
    p = []
    more = []

    for n in nums:
        if n < pivot:
            less.append(n)
        elif n == pivot:
            p.append(n)
        else:
            more.append(n)

    return less + p + more

nums = [9,12,5,10,14,3,10]
pivot = 10
print(pivotArray(nums, pivot))