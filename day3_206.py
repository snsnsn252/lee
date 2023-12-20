# 206
# https://leetcode.com/problems/reverse-linked-list/


# iterative, two pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    

# recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # recursion
    # the same as two pointer

    # temp is a new curr
    # then
    # move prev to curr position
    # move curr to a new curr position

    def reverse(self, curr, prev):
        if not curr:    # the end conition, curr is None
            return prev     # prev will be the tail

        temp = curr.next
        curr.next = prev

        return self.reverse(temp, curr)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.reverse(head, None)
    

# recursion
