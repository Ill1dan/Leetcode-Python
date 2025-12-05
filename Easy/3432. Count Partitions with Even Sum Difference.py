def countPartitions(self, nums):
        return 0 if sum(nums) % 2 else len(nums) - 1