# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node, canRob):
            if not node:
                return 0
            if not canRob:
                return dp(node.left, True) + dp(node.right, True)

            rob = node.val + (dp(node.left, False) + dp(node.right, False))
            dontRob = dp(node.left, True) + dp(node.right, True)
            return max(rob, dontRob)
        
        return dp(root, True)