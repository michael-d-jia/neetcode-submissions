# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        left = head
        right = head.next
        while left != None and right != None:
            if left is right:
                return True

            left = left.next
            if right.next != None and right.next.next != None:
                right = right.next.next
            else:
                return False
        
        return False