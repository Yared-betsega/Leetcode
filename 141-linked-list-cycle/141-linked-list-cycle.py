# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node:
            if node.val == "x":
                return True
            node.val = "x"
            node = node.next
        return False