# 106
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# compare the length and move the curr to the same position to the tail

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        if lenA >= lenB:
            headA = self.moveForward(headA, lenA - lenB)
        else:
            headB = self.moveForward(headB, lenB - lenA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def moveForward(self, head: ListNode, steps:int) -> ListNode:
        while steps > 0:
            head = head.next
            steps -= 1
        return head