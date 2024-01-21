# 151
# https://leetcode.com/problems/reverse-words-in-a-string/description/
# cannot finish

class Solution:

    # reverse the string
    def reverse(self, s:str, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    def removeSpace(self, s:str):
        s = list(s)
        slow = 0
        fast = 0
        while fast < len(s):
            if s[fast] != ' ':
                if slow != 0:
                    s[slow] = ' '
                    slow += 1
                while fast < len(s) and s[fast] != ' ':
                    s[slow] = s[fast]
                    slow += 1
                    fast += 1
            else:
                fast += 1
        return ''.join(s[:slow]) # convert back to string

    def reverseWords(self, s: str) -> str:
        s = self.removeSpace(s)
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        start = 0

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                self.reverse(s, start, i - 1)
                start = i + 1
        return ''.join(s)