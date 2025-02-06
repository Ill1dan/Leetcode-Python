from collections import defaultdict

def tupleSameProduct(nums):
    product_cnt = defaultdict(int)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            product = nums[i] * nums[j]
            product_cnt[product] += 1

    res = 0
    for cnt in product_cnt.values():
        pairs = (cnt * (cnt - 1)) // 2
        res += 8 * pairs

    return res


nums = [2,3,4,6]
print(tupleSameProduct(nums))