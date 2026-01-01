class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in digits:
            num=num*10+i
        num=num+1
        res=[]
        while num>0:
            res.append(num%10)
            num//=10
        return res[::-1]