import math

def minimumSize(nums, maxOperations):
    def can_divide(max_balls):
        ops = 0
        for n in nums:
            ops += math.ceil(n / max_balls) - 1
            if ops > maxOperations:
                return False
        return True

    l, r = 1, max(nums)
    res = r

    while l < r:
        mid = l + ((r - l) // 2)
        if can_divide(mid):
            r = mid
            res = r
        else:
            l = mid + 1

    return res

nums = [2,4,8,2]
maxOperations = 4
print(minimumSize(nums, maxOperations))