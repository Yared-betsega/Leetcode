# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 0
        prev = ListNode()
        node = head
        while node:
            prevChecker = ListNode(0, head)
            checker = head
            found = False
            for j in range(i):
                if checker.val > node.val:
                    prev.next = node.next
                    node.next = checker
                    prevChecker.next = node
                    node = prev.next
                    found = True
                    if j == 0:
                        head = prevChecker.next
                    break
                prevChecker = prevChecker.next
                checker = checker.next 
            if not found:
                prev = node
                node = node.next if node else None
            i += 1
            
        return head