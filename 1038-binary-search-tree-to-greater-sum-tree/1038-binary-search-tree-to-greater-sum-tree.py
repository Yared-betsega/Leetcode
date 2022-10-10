# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, prev):
            if not node:
                return 0
            
            right = dfs(node.right, prev)
            node.val += right + prev
            left = dfs(node.left, node.val)
            
            return node.val + left - prev
        dfs(root, 0)
        return root