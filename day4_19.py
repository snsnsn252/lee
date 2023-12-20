# 19
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # fast pointer move n + 1 steps
        # slow and fast pointers move together until fast point is NULL
        # slow pointer is the node before the target one
        
        dummy_head = ListNode(next = head)
        fast = dummy_head
        slow = dummy_head

        for i in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next    # slow is at the position prior to the target now
        
        slow.next = slow.next.next

        return dummy_head.next  # if there is only one node and it was deleted, it should be NULL
