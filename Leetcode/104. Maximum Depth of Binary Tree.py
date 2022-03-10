# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, cnt):
            if node:
                cnt += 1
                self.maxim = max(cnt, self.maxim)
                dfs(node.left, cnt)
                dfs(node.right, cnt)
                cnt -= 1
        self.maxim = 0
        dfs(root, 0)
        return self.maxim
                