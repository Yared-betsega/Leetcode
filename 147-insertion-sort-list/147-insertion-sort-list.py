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
            position_updated = False
            for j in range(i):
                if checker.val > node.val:
                    prev.next = node.next
                    node.next = checker
                    prevChecker.next = node
                    node = prev.next
                    if j == 0:
                        head = prevChecker.next
                    position_updated = True
                    break
                prevChecker = prevChecker.next
                checker = checker.next 
            if not position_updated:
                prev = node
                node = node.next if node else None
            i += 1
            
        return head
    
# time and space complexity
# time: O(n**2)
# space: O(1)