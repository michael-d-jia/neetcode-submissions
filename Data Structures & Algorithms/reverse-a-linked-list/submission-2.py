# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1, 2, 3, 4, 5]
        prev, curr = None, head
        # prev = None
        # curr = 1 -> 2

        while curr:
            # temp = 2 -> 3
            temp = curr.next
            # curr.next = None
            curr.next = prev
            # prev = 1 -> None
            prev = curr
            # curr = 2 -> 3
            curr = temp


        return prev