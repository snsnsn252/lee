# 20
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')
            elif not stack or stack[-1] != char:    # 1: less right brackets 2: wrong sequence
                return False
            else:
                stack.pop()
        
        return True if not stack else False     # 3: more right brackets