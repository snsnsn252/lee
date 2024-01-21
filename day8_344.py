# 344
# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        n = len(s)
        for i in range(n//2):
            s[i], s[n - 1 - i] = s[n - 1 - i], s[i] 
            
            # two pointers
            #swap: left = s[i], right = s[n - 1 - i]
            # if odd, the middle does not change