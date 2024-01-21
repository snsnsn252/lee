# 349
# https://leetcode.com/problems/intersection-of-two-arrays/description/

# set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # iterate nums1 and create key-value pairs in table dictionary
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1 # if num exits, get the value; if not, get 0 + 1
        
        res = set()
        for num in nums2:
            if num in table: # if table.get(num) is not None # if num in table.keys()
                res.add(num)
                del table[num]
        
        return list(res)


# list
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        res = []

        for i in range(len(nums1)):
            count1[nums1[i]] += 1    # the num is the index in the list
        for j in range(len(nums2)):
            count2[nums2[j]] += 1
        
        for k in range(1001):
            if count1[k] * count2[k] > 0:   # check if the num is in both lists
                res.append(k)
        
        return res

