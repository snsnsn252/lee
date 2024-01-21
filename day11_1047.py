# 1047
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = list()

        for char in s:
            if (not stack) or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
            
        return ''.join(stack)