# 203
# https://leetcode.com/problems/remove-linked-list-elements/description/


# head and other nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while (head is not None and head.val == val):
            head = head.next
        
        cur = head
        while (cur is not None and cur.next is not None):   # check whether reached the last node
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head


# dummy head
# treat the head node as a regular node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummyhead = ListNode(0)
        dummyhead.next = head

        cur = dummyhead
        while cur is not None and cur.next is not None:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                
        return dummyhead.next