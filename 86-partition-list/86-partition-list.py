# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        lessThan, moreThan = ListNode(), ListNode()
        startOfLessThan, startOfMoreThan = lessThan, moreThan
        node = head
        while node:
            if node.val < x:
                lessThan.next = node
                lessThan = lessThan.next
            else:
                moreThan.next = node
                moreThan = moreThan.next
            node = node.next
        lessThan.next = startOfMoreThan.next
        moreThan.next = None
        return  startOfLessThan.next
    
# time and space complexity
# time: O(n)
# space: O(1)