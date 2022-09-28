# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        ct = 0
        while node:
            node = node.next
            ct += 1
        toBeDeleted = ct - n + 1
        
        start = prev = ListNode()
        node = head
        c = 1
        while node:
            if c == toBeDeleted:
                prev.next = node.next
            else:
                prev.next = node
            prev, node = node, node.next
            c += 1
            
        return start.next
            