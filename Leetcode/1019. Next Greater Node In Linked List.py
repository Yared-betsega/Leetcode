# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node = head
        stack = [node]
        greater = {}
        node = node.next
        while node:
            if node.val <= stack[-1].val:
                stack.append(node)
            else:
                while stack and node.val > stack[-1].val:
                    tempNode = stack.pop()
                    greater[tempNode] = node.val
                stack.append(node)
            node = node.next
        # print(stack)
        for node in stack:
            greater[node] = 0
        repo = []
        while head:
            repo.append(greater[head])
            head = head.next
            
        return repo
            
