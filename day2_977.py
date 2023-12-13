# 977
# https://leetcode.com/problems/squares-of-a-sorted-array/

# brute force
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x*x for x in nums)
    

# two pointer
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        i = 0
        j = n - 1 # i and j start from two position of the list, and become closer to the middle

        for k in range(n - 1, -1, -1): # -1 is excluded
            if abs(nums[i]) >= abs(nums[j]):
                res[k] = nums[i]*nums[i]
                i += 1
            else:
                res[k] = nums[j]*nums[j]
                j -= 1
        return res



