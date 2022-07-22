# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = start = ListNode(-200) # because node.val cannot be less than -100 so this can be used for some purposes later
        node = head
        while node and node.next:
            if node.val != node.next.val:
                prev = node
                node = node.next
            else:
                while node.next and node.val == node.next.val: # remove same elements
                    node = node.next
                prev.next = node.next 
                node = node.next
            if not start.next: # if elements in front are repeated it will be handled here
                start.next = prev if start.val != prev.val else None
        return start.next
    
# time and space complexity
# time: O(n)
# space: O(1)