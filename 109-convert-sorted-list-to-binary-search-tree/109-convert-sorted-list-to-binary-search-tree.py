# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        def construct(start, length):
            if length == 0:
                return None
            if length == 1:
                return TreeNode(start.val)
            ctr = 1
            nd = start
            while ctr < (length // 2) + 1:
                nd = nd.next
                ctr += 1
            node = TreeNode(nd.val)
            # print(nd.val, nd.next.val)
            node.left = construct(start, ctr - 1)
            node.right = construct(nd.next, length - ctr)
            return node
            
        return construct(head, length)
            