# 142
# https://leetcode.com/problems/linked-list-cycle-ii/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: # if there is a cycle, they will meet
                index1 = fast
                index2 = head

                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1

        return None # if there is no cycle