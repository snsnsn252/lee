# 209
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

# sliding window
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sub = 0
        i,j = 0, 0
        res = float('inf') # suppose it is the largest number
        length = 0

        for i in range(len(nums)):  # fix the tail i
            sub += nums[i]
            while (sub >= target):
                length = i - j + 1  # current length
                res = min(res, length)
                sub -= nums[j]
                j += 1  # move the start point j to minimize the window from j to i
                      
        return 0 if res == float('inf') else res
            
