# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        node = head
        answer = ListNode()
        temp = answer
        while node:
            for i in range(k):
                stack.append(node)
                node = node.next
                if not node:
                    break

            if len(stack) < k:
                for link in stack:
                    temp.next = link
                    temp = temp.next
            else:
                while stack:
                    temp.next = stack.pop()
                    temp = temp.next
                    
        temp.next = None
        
        return answer.next

# time and space complexity
# time complexity = O(nk)
# space complexity = O(n)
                
