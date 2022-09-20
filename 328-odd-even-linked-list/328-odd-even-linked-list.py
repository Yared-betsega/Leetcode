# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        odd = oddStart = ListNode()
        even = evenStart = ListNode()
        oddIndex = head
        evenIndex = head.next
        while oddIndex:
            odd.next = oddIndex
            even.next = evenIndex
            odd, even = odd.next, even.next
            
            oddIndex = evenIndex.next if evenIndex else None
            evenIndex = oddIndex.next if oddIndex else None
            
        odd.next = evenStart.next
        return oddStart.next 
    
# time and space complexity
# time: O(n)
# space: O(1)
        