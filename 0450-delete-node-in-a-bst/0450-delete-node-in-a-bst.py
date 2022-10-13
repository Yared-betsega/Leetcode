# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node, prev = root, None
        while node and node.val != key:
            if node.val < key:
                prev, node = node, node.right
            else:
                prev, node = node, node.left
        
        if not node:
            return root
        if node.right:
            head = node.right
            while head.left:
                head = head.left
            head.left = node.left
        else: node.right = node.left
        if node.val == root.val:
            return root.right
        if node.val > prev.val:
            prev.right = node.right
        else:
            prev.left = node.right
        return root
        