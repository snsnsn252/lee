# 347
# https://leetcode.com/problems/top-k-frequent-elements/description/

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # priority queue

        # map: key-actual value, value-counts
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        
        pri_que = []

        for key, freq in mp.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
            
        result = [0] * k
        for i in range(k -1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result