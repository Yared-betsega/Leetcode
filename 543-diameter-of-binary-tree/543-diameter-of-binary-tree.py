# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _max = [0]
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            _max[0] = max(_max[0], left + right)
            return max(left, right) + 1
        
        dfs(root)
        return _max[0]
            
