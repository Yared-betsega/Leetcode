# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        def sort(cur, l1, l2):
            if not l1:
                cur.next = l2
                return 
            elif not l2:
                cur.next = l1
                return 
            
            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next
                sort(cur, l1.next, l2)
            else:
                cur.next = l2
                cur = cur.next
                sort(cur, l1, l2.next)
        cur = start = ListNode()
        sort(cur, list1, list2)
        return start.next