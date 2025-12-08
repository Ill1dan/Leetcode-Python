class Solution(object):
    def countTriples(self, n):
        cnt = 0

        for i in range(1, n + 1):
            a = i * i
            for j in range(i + 1, n + 1):
                b = j * j
                rootDouble = sqrt(a + b)
                rootInt = (int(sqrt(a + b)))

                if (rootDouble == rootInt and rootInt <= n):
                    cnt += 1
    
        return cnt * 2