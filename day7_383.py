# 383
# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}

        for char in magazine:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        for char in ransomNote:
            if hashmap.get(char, 0) == 0:
                return False
            hashmap[char] -= 1

        return True

# only contains 26 words, could use [0]*26 instead of map