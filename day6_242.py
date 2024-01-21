# 242
# https://leetcode.com/problems/valid-anagram/description/

# Hash Table: array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for x in s:
            count[ord(x) - ord('a')] += 1
            # ord(): ASCII 
            # ord(x) - ord('a'): subtract the value for x
            # index a = 0, b = 1, c = 2, .... z = 25
        
        for x in t:
            count[ord(x) - ord('a')] -= 1
            # if there is the same char, deducted
        
        for val in count:
            if val != 0:
                return False
        return True