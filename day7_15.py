# 15
# https://leetcode.com/problems/3sum/description/

# two pointer + deduplication
# sort -> i left x x x x x x right

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:  # if [i, i, x,x,x,x,...]
                continue

            # two pointer for the remaining numbers
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if a + nums[left] + nums[right] < 0:
                    left += 1
                elif a + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1   
                    
                    # only need to change one pointer, the equation will do it self to deduplicate
                    # [-2, -2, 0, 0, 2, 2]
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
