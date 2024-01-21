# 1
# https://leetcode.com/problems/two-sum/description/

# map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = {}

        for index, value in enumerate(nums):
            if target - value in records: # containskey
                return [records[target - value], index] 
            records[value] = index
        return []

        # save key=num value, value=index