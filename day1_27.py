# 27
# https://leetcode.com/problems/remove-element/

# two pointers
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):       # fast points to the values and only choose what we want
            if (nums[fast] != val):     # fast will not verify what we want to remove
                nums[slow] = nums[fast]     # slow points to the position and rewrite the valid values from fast
                slow += 1
        return slow
    

# brute force
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                for j in range(i + 1, n):       # once there is a val, move the following array forward one position
                    nums[j - 1] = nums[j]
                i -= 1      # index move forward correspondingly
                n -= 1      # size - 1 correspondingly
            i += 1
        return n
                   