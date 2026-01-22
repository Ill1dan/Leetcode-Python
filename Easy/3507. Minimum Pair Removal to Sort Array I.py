class Solution(object):
    def minimumPairRemoval(self, nums):
        count = 0

        # This while loop keeps running until:
        # 1) the array becomes non-decreasing, or
        # 2) the array size becomes 1 (everything got merged)
        while len(nums) > 1:
            isSorted = True
            minSum = float('inf')  # tracks the minimum adjacent pair sum
            targetIndex = -1      # index of the left element of that pair

            # Traverse all adjacent pairs
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]

                # Check if array is still sorted
                if nums[i] > nums[i + 1]:
                    isSorted = False  # array is not sorted yet

                # Use strictly less to pick the leftmost pair
                # If the problem asked for the rightmost one,
                # we would use (s <= minSum) instead
                if s < minSum:
                    minSum = s
                    targetIndex = i

            # If the array is already sorted, stop the simulation
            if isSorted:
                break

            count += 1

            # Replace the left element of the pair with their sum
            nums[targetIndex] = minSum

            # Remove the right element of the pair
            # Array length reduces here
            nums.pop(targetIndex + 1)

        return count
        