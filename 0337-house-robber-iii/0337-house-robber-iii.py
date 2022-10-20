# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
#         def dp(node, canRob):
#             if not node:
#                 return 0
#             if not canRob:
#                 return dp(node.left, True) + dp(node.right, True)

#             rob = node.val + (dp(node.left, False) + dp(node.right, False))
#             dontRob = dp(node.left, True) + dp(node.right, True)
#             return max(rob, dontRob)
        
#         return dp(root, True)
            
        def dfs(node):
            if not node: return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob = node.val + left[1] + right[1]
            dontRob = max(left) + max(right)
            return [rob, dontRob]
        
        return max(dfs(root))
    
        