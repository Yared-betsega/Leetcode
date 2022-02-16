# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        repo = []
        while head:
            repo.append(head.val)
            head = head.next
        repo.pop(len(repo) - n)
        
        head = node = None
        for i in repo:
            temp = ListNode(i)
            if not head:
                head = temp 
                node = head
            else:
                node.next = temp
                node = temp
        return head  
