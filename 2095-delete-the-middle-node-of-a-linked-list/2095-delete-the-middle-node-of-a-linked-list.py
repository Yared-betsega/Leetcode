# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = start = ListNode(0)
        fast = slow = head
        while fast and fast.next:
            prev.next = slow
            prev = prev.next
            fast, slow = fast.next.next, slow.next
        prev.next = slow.next
        return start.next

# time and space complexity
# time: O(n)
# space: O(1)