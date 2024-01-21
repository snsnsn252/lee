# 454
# https://leetcode.com/problems/4sum-ii/description/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in hashmap:
                    hashmap[n1 + n2] += 1
                else:
                    hashmap[n1+ n2] = 1
        
        count = 0

        for n3 in nums3:
            for n4 in nums4:
                key = 0 - (n3 + n4)     # n1 + n2 + n3 + n4 = 0     #sum is key, count is value
                if key in hashmap:
                    count += hashmap[key]
        return count

