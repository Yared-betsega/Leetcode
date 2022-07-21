# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first, second = head, head.next
        while second:
            first.val, second.val = second.val, first.val
            first = second.next
            second = first.next if first else None
        
        return head
        
    # time and space complexity
    # time: O(n)
    # space: O(1)