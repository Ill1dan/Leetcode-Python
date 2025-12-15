class Solution(object):
    def getDescentPeriods(self, prices):
        n = len(prices)
        result = 0
        i = 0
        
        while i < n:
            j = i
            
            while j + 1 < n and prices[j] - prices[j+1] == 1:
                j += 1
            
            length = j - i + 1
            result += length * (length + 1) // 2
            
            i = j + 1
            
        return result
        