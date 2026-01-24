class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        start, end = 0, len(nums) - 1
        max_pair = 0

        while start < end:
            pair_sum = nums[start] + nums[end]
            max_pair = max(max_pair, pair_sum)
            start += 1
            end -= 1

        return max_pair
        