# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        lst.sort()
        head = node = ListNode(lst[0], None)
        
        for num in lst[1:]:
            node.next = ListNode(num, None)
            node = node.next
        
        return head

# time and space complexity 
# time complexity = O(nlog(n))
# space complexity = O(n)
