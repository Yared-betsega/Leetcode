# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode()
        node = head
        head = prev
        added = set()
        rep = set()
        while node:
            if node.val in added: 
                prev.next = node.next
                rep.add(node.val)
                node = prev.next
            else:
                prev.next = node
                prev = node
                node = node.next
                added.add(prev.val)
        prev = head
        node = head.next
        while node:
            if node.val in rep:
                prev.next = node.next
                node = prev.next
            else:
                prev.next = node
                prev = node
                node = node.next
        return head.next