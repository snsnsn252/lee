# 541
# https://leetcode.com/problems/reverse-string-ii/description/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        def sub(text):
            n = len(text)
            for i in range(n//2):
                text[i], text[n - 1 - i] = text[n - 1 - i], text[i]
            return text

        res = list(s)   #converting String to List

        for cur in range(0, len(s), 2 * k): #This loop iterates through the string in segments of 2k characters
            res[cur : cur + k] = sub(res[cur : cur + k])
        
        return ''.join(res) # convert list to string