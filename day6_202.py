# 202
# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()

        while True:
            n = self.getsum(n)
            if n == 1:
                return True

            if n in res:
                return False
            else:
                res.add(n)
        
    def getsum(self, n:int) -> int:
        if n == 0:
            return 0
        else:
            return (n % 10)**2 + self.getsum(n // 10)
        
        # n = 123
        # n % 10 = 3
        # n // 10 = 12
          

