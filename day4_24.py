# 24
# https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # draw!

        dummy_head = ListNode(next = head)  # 0
        curr = dummy_head

        while curr.next and curr.next.next:
            temp = curr.next    # 1
            temp1 = curr.next.next.next # 3, the following pair

            curr.next = curr.next.next  # dummy -> 2
            curr.next.next = temp   # 2 -> 1
            temp.next = temp1   # 1 -> 3

            # move curr to deal with the following pair
            curr = curr.next.next
        return dummy_head.next
