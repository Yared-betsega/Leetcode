# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        items_to_be_reversed = []
        node = head
        i = 0
        while node:
            if i >= left - 1 and i <= right - 1:
                items_to_be_reversed.append(node.val)
            node = node.next
            i+=1
        
        node = head
        i, j = 0, len(items_to_be_reversed) - 1
        while node:
            if i >= left - 1 and i <= right - 1:
                node.val = items_to_be_reversed[j]
                j -= 1
            node = node.next
            i+=1
        
        return head
            