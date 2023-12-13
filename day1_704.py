# 704
# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while (left <= right):      #[left, right], right is valid
            mid = left + (right - left)//2      # overflow
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else: 
                return mid
        return -1
    

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while (left < right):       # [left, right), right is not valid, [1,1)
            mid = left + (right - left)//2
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid     # since right is not valid, it is ok to use it
            else:
                return mid
        return -1