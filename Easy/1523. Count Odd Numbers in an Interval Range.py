class Solution(object):
    def countOdds(self, low, high):
        count = 0
        if high % 2 != 0:
            count += 1
            high -= 1
        if low % 2 != 0:
            count += 1
            low += 1
        count += (high - low) // 2
        return count
        