"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head

        current_old = head
        old_to_new = {None: None}
        while current_old:
            old_to_new[current_old] = Node(current_old.val)
            current_old = current_old.next

        current_old = head

        while current_old:
            old_to_new[current_old].next = old_to_new[current_old.next]
            old_to_new[current_old].random = old_to_new[current_old.random]
            current_old = current_old.next

        return old_to_new[head]