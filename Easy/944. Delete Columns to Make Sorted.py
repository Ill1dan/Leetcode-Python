class Solution(object):
    def minDeletionSize(self, strs):
        count = 0
        rows = len(strs)
        cols = len(strs[0])

        for col in range(cols):
            for row in range(1,rows):
                if strs[row][col] < strs[row-1][col]:
                    count+=1
                    break
        return count          
        